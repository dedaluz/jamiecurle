import re
from django import template
from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.cache import cache
register = template.Library()
from textile import textile
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer, LEXERS


class FieldRender(template.Node):
    
    def __init__(self, obj_and_field):
        self.obj = template.Variable(obj_and_field.split('.')[0])
        self.t = obj_and_field.split('.')[1]
    
    
    def render(self, context):
        # at some stage in the future I want to ditch beautiful soup
        self_closing_tags = ['true']
        # try the cache first
        obj = self.obj.resolve(context)
        # now we have the object see if it's in the cache
        key = '%s_%s_%s' % (self.obj, self.t, obj.pk)
        cached = cache.get(key)
        if 'no-cache' not in context.get('request').GET.keys() and cache.get(key) is not None:
            return mark_safe(cached)
        # it's not in the cache so make it
        t = template.Template(getattr(obj, self.t))
        content  = t.render(context)
        #
        #
        # set up soup
        soup = BeautifulSoup(unicode(content))
        #
        #
        # now we've got formatted syntax that is going to get mangled by markdown so lets save it
        rendered_blocks = soup.findAll(u'div', u'source')
        for block in rendered_blocks:
            # here's one I prepared earlier
            block.replaceWith(u'<div class="bluepeter">HI</code>')
        # on with the other
        #
        #
        code_blocks = soup.findAll(u'code')
        for block in code_blocks:
            block.replaceWith(u'<code class="removed"></code>')
        # Run the content through textile.
        markeddown = mark_safe(force_unicode(textile(smart_str(unicode(soup)), encoding='utf-8', output='utf-8')))
        
        # Replace the pulled code blocks with syntax-highlighted versions.
        soup = BeautifulSoup(markeddown)
        empty_code_blocks, index = soup.findAll(u'code', u'removed'), 0
        formatter = HtmlFormatter(cssclass=u'source')
        
        
        for block in code_blocks:
            if block.has_key(u'class'):
                # <code class='python'>python code</code>
                language = block[u'class']
            else:
                # <code>plain text, whitespace-preserved</code>
                language = u'text'
            try:
                lexer = get_lexer_by_name(language, stripnl=False, encoding=u'UTF-8')
            except ValueError, e:
                try:
                    # Guess a lexer by the contents of the block.
                    lexer = guess_lexer(block.renderContents())
                except ValueError, e:
                    # Just make it plain text.
                    lexer = get_lexer_by_name(u'text', stripnl=False, encoding=u'UTF-8')
            empty_code_blocks[index].replaceWith(highlight(block.renderContents(), lexer, formatter))
            index = index + 1
        
        #
        #
        # replace the pre-rendered code blocks
        for i, code_block in enumerate(soup.findAll(u'div', u'bluepeter')):
            code_block.replaceWith(rendered_blocks[i])
        #
        #
        # finally do the media url
        soup = re.sub('{{MEDIA_URL}}', settings.MEDIA_URL, unicode(soup))
        # set the cache
        if 'no-cache' not in context.get('request').GET.keys():
            cache.set(key, soup, 300)
        
        return mark_safe(soup)
        
@register.tag
def render_field(parser, token):
    bits = token.contents.split()
    # remove tag name
    bits.pop(0)
    # assign the template
    field = bits.pop(0)
    #
    return FieldRender(field)



class RenderAssetNode(template.Node):
    
    def __init__(self, obj, asset_type):
        self.rendered_assets = []
        self.asset_type = 'js' if asset_type == 'js' else 'css'
        self.obj = template.Variable(obj)
        self.obj_name = obj
    
    def css(self):
        return '<style type="text/css">\n%s\n</style>' % '\n'.join(self.rendered_assets)
    
    def javascript(self):
        return '<script type="text/javascript">\n%s\n</script>' % '\n'.join(self.rendered_assets)
    
    def render(self, context):
        obj =  self.obj.resolve(context)
        context = template.Context({
            self.obj_name : obj,
            'MEDIA_URL' : settings.MEDIA_URL
            })
        assets = obj.stylesheets.all() if self.asset_type == 'css' else obj.scripts.all()
        
        for asset in assets:
            t = template.loader.get_template(asset.template)
            self.rendered_assets.append('\n %s' % t.render(context))
            
        if len(self.rendered_assets) > 0:
            return self.css() if self.asset_type == 'css' else self.javascript()
        return ''
    


@register.tag
def render_asset(parser, token):
    bits = token.contents.split()
    return RenderAssetNode(bits[1], bits[2])
    

