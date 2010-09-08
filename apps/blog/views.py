# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import Post

def archive(request):
    posts = Post.objects.all()
    featured = posts.filter(featured=True)[0]
    posts = posts.exclude(pk__in=[featured.pk])
    return render_to_response('blog/archive.html', RequestContext(request, {
        'posts' : posts,
        'featured':featured
    }))

def year(request, year):
    return render_to_response('blog/year.html', RequestContext(request, { }))

def month(request, year, month):
    return render_to_response('blog/month.html', RequestContext(request, { }))

def post(request,  year, month, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/post.html', RequestContext(request, {
        'post' : post
    }))
