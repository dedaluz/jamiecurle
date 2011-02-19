# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import inlineformset_factory
from taggit.models import Tag
from forms import BlogPostForm, BlogImageForm
from models import BlogPost, BlogImage


def create(request):
    
    
    BlogImageFormSet = inlineformset_factory(BlogPost,BlogImage, form=BlogImageForm, extra=1)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        blogimage_formset = BlogImageFormSet(request.POST, request.FILES, prefix="blogimage")
        
        if form.is_valid():
            blogpost = form.save()
            if blogimage_formset.is_valid():
                blogimages = blogimage_formset.save()
        
        print form.errors
        print blogimage_formset.errors
        #print blogpost, blogimages
    
    if request.method == 'GET':
        form = BlogPostForm()
        blogimage_formset = BlogImageFormSet(prefix="blogimage")
    
    return render_to_response('posts/create.html', RequestContext(request,{
        'form' : form,
        'blogimage_formset' : blogimage_formset 
    }))

def post(request, slug):
    pass

def index(request):
    return render_to_response('posts/index.html', RequestContext(request,{}))

