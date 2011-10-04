# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import inlineformset_factory
from taggit.models import Tag
from django.conf import settings
from forms import BlogPostForm, BlogImageForm
from models import BlogPost, BlogImage
from django.views.decorators.cache import cache_page






def index(request):
    posts = BlogPost.objects.for_user(request.user)[:19]
    return TemplateResponse(request, 'posts/index.html', {
        'posts' : posts
    })



def show(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    # if user not authed and post not published then 404
    if request.META['REMOTE_ADDR'] not in getattr(settings, 'STATS_IGNORE_IPS', []) :
        post.views +=1
        post.save()
    
    if not request.user.is_authenticated() and post.status != BlogPost.PUBLISHED:
        raise Http404('Post is not publiced')
    
    return TemplateResponse(request, 'posts/show.html', {
        'post' : post,
    })


def archive_month(request, year, month):
    posts = BlogPost.objects.for_user(request.user).order_by('created').filter(created__year=year, created__month=month)
    
    year = int(year)
    month = int(month)
    month = datetime.date(year=year,month=month,day=1)
    
    return TemplateResponse(request, 'posts/archive_month.html', {
        'posts' : posts,
        'year' : year,
        'month' : month
    })

def archive_year(request, year):
    # custom sql to get the months and a count
    cursor = connection.cursor()
    cursor.execute("""SELECT MONTH(created), COUNT(*)
            FROM posts_blogpost
            WHERE `created` BETWEEN '%(year)s-01-01' AND '%(year)s-12-31' 
            GROUP BY MONTH(created);""" % {'year': year} 
        )
    months = cursor.fetchall()
    return TemplateResponse(request, 'posts/archive_year.html', {
        'months' : months,
        'year' : year
    })

