import re
from django import template
register = template.Library()
from textile import textile
from BeautifulSoup import BeautifulSoup



class ContentNode(template.Node):
    
    def __init__(self, t, c):
        self.context_name = t.split('.').pop()
        self.t = template.Variable(t)
        self.c = c
        
        
    def render(self, context):
        # make t
        t = template.Template(self.t.resolve(context))
        # build c
        c = {}
        for obj in self.c:
            key = obj
            value = template.Variable(obj)
            c.update({
                key : value.resolve(context)
            })
        context[self.context_name] = t.render(template.Context(c))
        return ''

@register.tag
def super_render(parser, token):
    bits = token.contents.split()
    # remove tag name
    bits.pop(0)
    # assign the template
    t = bits.pop(0)
    return ContentNode(t,bits)