# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from apps.blog.models import Post
from apps.books.models import Book
from apps.info.models import Page

def home(request):
    posts = Post.objects.filter(status=Post.PUBLISHED)
    try:
        featured = Post.objects.filter(featured=True)[0]
        posts = posts.exclude(pk__in=[featured.pk])
    except IndexError:
        pass
    
    books = Book.objects.all()
    pages = Page.objects.filter(status=Page.PUBLISHED)
    return render_to_response('home.html', RequestContext(request, {
        'posts' : posts,
        'featured' : featured,
        'books' : books,
        'pages' : pages,
    }))