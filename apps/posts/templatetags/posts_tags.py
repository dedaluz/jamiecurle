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


"""
temps and sunlight as hue and saturation calculated
as the average amount for NE England according to met
office data
"""
colours = [
    (255.0,27.7126443311),
    (245.578313253,34.2094985159),
    (203.248995984,49.2263282726),
    (154.297188755,61.2968854298),
    (95.9748995984,72.8323699422),
    (34.8704819277,75.0),
    (0.0,70.2606837,50),
    (7.51004016064,66.8215903765),
    (52.7921686747,56.165939981),
    (124.598393574,44.4600275525),
    (200.859437751,31.5213531977),
    (241.8062249,25.0),
]
@register.filter
def color_for_date(date):
    # get the month
    current = colours[date.month - 1 ]
    days_in_month = calendar.monthrange(date.year, date.month)
    days_in_month = days_in_month[1]
    # 
    try:
        next = colours[date.month]
    except IndexError:
        next = colours[0]
    hue_delta = next[0] - current[0]
    sat_delta = next[1] - current[1]
    hue_per_day = hue_delta / days_in_month
    sat_per_day = sat_delta / days_in_month
    hue = current[0] + (date.day * hue_per_day)
    sat = current[1] + (date.day * sat_per_day)
    
    return 'hsla(%s,%s%%,50%%, 1)' % (hue, sat)

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