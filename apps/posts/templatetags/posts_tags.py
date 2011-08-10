import re 
import pygments
import calendar
from django import template 
from pygments import lexers 
from pygments import formatters
from django.contrib.markup.templatetags.markup import markdown
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
    regex = re.compile(r'<code(.*?)>(.*?)</code>', re.DOTALL)
    # split it up into lang chunks
    last_end = 0 
    to_return = '' 
    found = 0
    
    
    for match_obj in regex.finditer(content):
        code_class = match_obj.group(1) 
        code_string = match_obj.group(2)
        if code_class.find('lang'): 
            language = re.split(r'"|\'', code_class)[1]
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
        pygmented_string = pygments.highlight(code_string, lexer, formatters.HtmlFormatter())
        to_return = to_return + markdown(content[last_end:match_obj.start(0)]) + pygmented_string
        last_end = match_obj.end(2) 
        found = found + 1 
    
    to_return = to_return + markdown(content[last_end:])
    # now process markdown
    #print to_return
    
    return to_return