import re 
import pygments
from django import template 
from pygments import lexers 
from pygments import formatters
from django.contrib.markup.templatetags.markup import markdown
from django.utils.safestring import mark_safe
from BeautifulSoup import BeautifulSoup
from apps.posts.models import BlogPost
 
register = template.Library()


@register.inclusion_tag('posts/_blog_nav.html', takes_context=True)
def blog_nav(context):
    articles = BlogPost.objects.filter(status=BlogPost.PUBLISHED).order_by('created')
    dates = articles.dates('created', 'month')
    archive = []
    
    for date in dates.reverse():
        archive.append((date, articles.filter(created__month=date.month, created__year=date.year).count()))
    
    return {'archive' : archive}


@register.filter
def month_name(month_num):
    return calendar.month_name[month_num]

@register.filter
def render(content):
    regex = re.compile(r'(<code(.*?)</code>)', re.DOTALL)
    code_blocks = []
    
    for i, m in enumerate(regex.finditer(content)):
        code = m.group(0)
        # if there is a lang attribute, use that
        if code.find('lang'):
            # get the language
            language = re.split(r'"|\'', code)[1]
            # fix some wonky lexers
            if language == 'conf': language = 'nginx'
            if language == 'regex': language = 'perl'
            # all goods
            lexer = lexers.get_lexer_by_name(language)
        else:
            try: 
                lexer = lexers.guess_lexer(str(code))
            except ValueError:
                lexer = lexers.PythonLexer()
        # remove the code tags
        code = code.replace('</code>', '')
        code = code.replace('<code>', '')
        code = re.sub('<code(.*?)>', '', code)
        # create the pygmented code with the lexer
        pygmented_string = pygments.highlight(code, lexer, formatters.HtmlFormatter())
        # put the code blocks into the list for processintg later
        code_blocks.append(pygmented_string)
        # replace the <code> tags with placeholders that can be used to replace
        content = content.replace(m.string[m.start():m.end()], '{{CODE%s}}' % i)
    
    # now process as markdown
    content = markdown(content)
    # replaced placeholders with the actual code
    for i, code in enumerate(code_blocks):
        content = content.replace('<p>{{CODE%s}}</p>' % i, code)
        content = content.replace('{{CODE%s}}' % i, code)
    # return
    return mark_safe(content)
render.is_safe = True