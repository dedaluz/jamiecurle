# -*- coding: utf-8 -*-
import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from apps.posts.models import BlogPost, BlogImage


def index(request):
    posts = BlogPost.objects.for_user(request.user)[:5]
    
    
    return render_to_response('home/index.html', RequestContext(request,{
        'posts' : posts,
    }))
