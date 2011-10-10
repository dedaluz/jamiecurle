import datetime
from django import template 
register = template.Library()
from apps.stats.models import Visit


class StatsForPathDateRangeNode(template.Node):
    
    def __init__(self, path, start_date, end_date, varname):
        self.path = template.Variable(path)
        self.start_date = start_date
        self.end_date = end_date
        self.varname = varname
    
    
    def render(self, context):
        path = self.path.resolve(context)
        visits = Visit.objects.views_for_path(path, self.start_date, self.end_date)
        context[self.varname] = 'asd'
        return ''
    

@register.tag
def stats_for_path(parser, token):
    bits = token.contents.split()
    start_date, end_date = Visit.objects.dates()
    start_date = start_date - datetime.timedelta(days=7)
    return StatsForPathDateRangeNode(bits[1], start_date, end_date, bits[2])

"""
# get the vists
start_date, end_date = Visit.objects.dates()
start_date = start - datetime.timedelta

print start_date, end_date

# last_seven_days

"""
