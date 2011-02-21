import re 
import pygments 
from django import template 
from pygments import lexers 
from pygments import formatters
from django.contrib.markup.templatetags.markup import markdown
from BeautifulSoup import BeautifulSoup
 
register = template.Library()

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
            lexer = lexers.get_lexer_by_name(language) 
        else: 
            try: 
                lexer = lexers.guess_lexer(str(code)) 
            except ValueError: 
                lexer = lexers.PythonLexer() 
        pygmented_string = pygments.highlight(code_string, lexer, formatters.HtmlFormatter()) 
        to_return = to_return + content[last_end:match_obj.start(0)] + pygmented_string 
        last_end = match_obj.end(2) 
        found = found + 1 
    to_return = to_return + content[last_end:]
    # now process markdown
    
    
    return markdown(to_return)
    