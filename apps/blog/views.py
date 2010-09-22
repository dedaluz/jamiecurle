# Create your views here.
import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import Post

def archive(request):
    posts = Post.objects.filter(status=Post.PUBLISHED)
    try:
        featured = posts.filter(featured=True)[0]
        posts = posts.exclude(pk__in=[featured.pk])
    except IndexError:
        featured = None
    # return
    return render_to_response('blog/archive.html', RequestContext(request, {
        'posts' : posts,
        'featured':featured
    }))


def month(request, year, month):
    posts = Post.objects.filter(status=Post.PUBLISHED, created__year=year, created__month=month)
    return render_to_response('blog/month.html', RequestContext(request, {
        'posts' : posts , 
        'view_date' : datetime.date(year=int(year), month=int(month), day=1) 
    }))

def post(request,  year, month, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'blog/post.html'
    if post.html:
        template = post.html
    return render_to_response(template, RequestContext(request, {
        'post' : post
    }))
