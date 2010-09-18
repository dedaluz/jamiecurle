import re
from django import template
register = template.Library()

from apps.blog.models import Post

@register.inclusion_tag('blog/_nav.html')
def blog_archive_nav():
    posts = Post.objects.filter(status=Post.PUBLISHED)
    months = posts.dates('created', 'month', order='DESC')
    nav = []
    for month in months:
        nav.append( (month, posts.filter(created__month=month.month).count()) )
    
    return {'nav': nav}

@register.filter
def get_range( value ):
  return range( value )

