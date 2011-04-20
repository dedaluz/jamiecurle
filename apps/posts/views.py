# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
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
    
    #print form.tags.media
    
    #
    # all done - return
    return TemplateResponse(request, 'posts/create_and_edit.html',{
        'form' : form,
        'blogimage_formset' : blogimage_formset 
    })


def show(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    
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
    months = BlogPost.objects.for_user(request.user).order_by('created').filter(created__year=year).dates('created', 'month')
    months = months.reverse()
    return TemplateResponse(request, 'posts/archive_year.html', {
        'months' : months,
        'year' : year
    })

