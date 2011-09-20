import calendar
import re
from django import template 
register = template.Library()

MENTION_RE = re.compile('(\@[a-zA-Z0-9]+)')

@register.filter
def parse_mentions(tweet):
    return tweet

@register.filter
def model(obj):
    return obj._meta.app_label

@register.inclusion_tag('utils/_thing.html')
def render_thing(thing):
    return{
        'thing' : thing
    }

class CollationNode(template.Node):
    
    def __init__(self, date, bookmarks, instagrams, scrobbles, tweets, varname):
        self.date = template.Variable(date)
        self.bookmarks = template.Variable(bookmarks)
        self.instagrams = template.Variable(instagrams)
        self.scrobbles = template.Variable(scrobbles)
        self.tweets = template.Variable(tweets)
        self.varname = varname
        
    
    
    def render(self, context):
        date = self.date.resolve(context)
        # populate today
        today = []
        today += self.bookmarks.resolve(context).filter(created__year=date.year, created__month=date.month, created__day=date.day)
        today += self.instagrams.resolve(context).filter(created__year=date.year, created__month=date.month, created__day=date.day)
        today += self.scrobbles.resolve(context).filter(created__year=date.year, created__month=date.month, created__day=date.day)
        today += self.tweets.resolve(context).filter(created__year=date.year, created__month=date.month, created__day=date.day)
        # nowe sort it by obj.created
        today = sorted(today, key=lambda obj : obj.created)
        context[self.varname] = today
        return ''


@register.tag
def day_as_list(parser, token):
    bits = token.contents.split()
    #print bits
    return CollationNode(bits[1], bits[2], bits[3], bits[4], bits[5], bits[7])
    

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
