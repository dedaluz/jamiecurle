import re
from django import template
register = template.Library()
from textile import textile
from BeautifulSoup import BeautifulSoup


from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer

from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.conf import settings


@register.filter
def get_range( value ):
  return range( value )


@register.filter
def render(content, safe="unsafe"):
    """Render this content for display."""

    # First, pull out all the <code></code> blocks, to keep them away
    # from Markdown (and preserve whitespace).
    soup = BeautifulSoup(unicode(content))
    code_blocks = soup.findAll(u'code')
    for block in code_blocks:
        block.replaceWith(u'<code class="removed"></code>')

    # Run the post through markdown.
    if safe == u"unsafe":
        safe_mode = False
    else:
        safe_mode = True
    markeddown = mark_safe(force_unicode(textile(smart_str(unicode(soup)), encoding='utf-8', output='utf-8')))
    # Replace the pulled code blocks with syntax-highlighted versions.
    soup = BeautifulSoup(markeddown)
    empty_code_blocks, index = soup.findAll(u'code', u'removed'), 0
    formatter = HtmlFormatter(cssclass=u'source')
    print len(code_blocks)
    print len(empty_code_blocks), index
    for block in code_blocks:
        if block.has_key(u'class'):
            # <code class='python'>python code</code>
            language = block[u'class']
        else:
            # <code>plain text, whitespace-preserved</code>
            language = u'text'
        try:
            lexer = get_lexer_by_name(language, stripnl=True, encoding=u'UTF-8')
        except ValueError, e:
            try:
                # Guess a lexer by the contents of the block.
                lexer = guess_lexer(block.renderContents())
            except ValueError, e:
                # Just make it plain text.
                lexer = get_lexer_by_name(u'text', stripnl=True, encoding=u'UTF-8')
       
        empty_code_blocks[index].replaceWith(highlight(block.renderContents(), lexer, formatter))
        index = index + 1
    
    soup = re.sub('{{MEDIA_URL}}', settings.MEDIA_URL, unicode(soup))
    return mark_safe(soup)


class RenderAssetNode(template.Node):
    
    def __init__(self, post, asset_type):
        self.rendered_assets = []
        self.asset_type = 'js' if asset_type == 'js' else 'css'
        self.post = template.Variable(post)
    
    def css(self):
        return '<style type="text/css">\n%s\n</style>' % '\n'.join(self.rendered_assets)
    
    def javascript(self):
        return '<script type="text/javascript">\n%s\n</script>' % '\n'.join(self.rendered_assets)
    
    def render(self, context):
        post =  self.post.resolve(context)
        context = template.Context({
            'post' : post,
            'MEDIA_URL' : settings.MEDIA_URL
            })
        
        assets = post.stylesheets.all() if self.asset_type == 'css' else post.scripts.all()

        
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
    

