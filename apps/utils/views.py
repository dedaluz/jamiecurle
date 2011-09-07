# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from apps.posts.models import BlogPost
from apps.instagram.models import InstagramPhoto


def index(request):
    posts = BlogPost.objects.for_user(request.user).order_by('-created')[:20]
    print InstagramPhoto.objects.count()
    instagrams = InstagramPhoto.objects.all()[:20]
    #creates = []
    #for post in posts:
    #    creates.append(post.created)
    #print creates
    return TemplateResponse(request, 'home/index.html', {
        'posts' : posts,
        'instagrams' : instagrams
    })
