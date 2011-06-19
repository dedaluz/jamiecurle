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
from forms import BlogPostForm, BlogImageForm
from models import BlogPost, BlogImage


@login_required
def create(request):
    return edit(request)

@login_required
def edit(request, slug=None):
    # create the obj is we have a slug
    instance = None
    if slug is not None:
        instance = get_object_or_404(BlogPost, slug=slug)
    # create the formsets
    BlogImageFormSet = inlineformset_factory(BlogPost,BlogImage,form=BlogImageForm, extra=3)
    #
    # process post
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=instance)
        blogimage_formset = BlogImageFormSet(request.POST, request.FILES, instance=instance, prefix="blogimage")
        # if we're all valid then proceed with creation
        if form.is_valid() and blogimage_formset.is_valid():
            # save the post
            blogpost = form.save()
            # if we have no instance then remake the formset using the new blogpost
            if instance is None:
                blogimage_formset = BlogImageFormSet(request.POST, request.FILES, instance=blogpost , prefix="blogimage")
            # save the images
            blogimages = blogimage_formset.save()
            # create the message
            # return the correct redirect
            return HttpResponseRedirect(reverse("posts:show", args=[blogpost.slug]))
    #
    # process a GET
    if request.method == 'GET':
        form = BlogPostForm(instance=instance)
        blogimage_formset = BlogImageFormSet(instance=instance, prefix="blogimage")
    
    #
    # all done - return
    return TemplateResponse(request, 'posts/create_and_edit.html',{
        'form' : form,
        'blogimage_formset' : blogimage_formset 
    })


def show(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    # if user not authed and post not published then 404
    
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

