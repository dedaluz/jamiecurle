# -*- coding: utf-8 -*-
import datetime
from django.template.response import TemplateResponse
from apps.blog.models import BlogPost
from apps.instagram.models import InstagramPhoto
from apps.pinboard.models import PinboardBookmark
from apps.lastfm.models import Scrobble
from apps.twitter.models import Tweet
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index(request):
    
    today = datetime.date.today()
    #date_list = [today - datetime.timedelta(days=x) for x in range(0,30) ]
    
    posts = BlogPost.objects.for_user(request.user).order_by('-created')[:20]
    #instagrams = InstagramPhoto.objects.filter(created__gt=date_list[-1])
    #bookmarks = PinboardBookmark.objects.filter(created__gt=date_list[-1])
    #scrobbles = Scrobble.objects.filter(created__gt=date_list[-1])
    #tweets = Tweet.objects.filter(created__gt=date_list[-1])
    #creates = []
    #for post in posts:
    #    creates.append(post.created)
    #print creates
    return TemplateResponse(request, 'home/index.html', {
        'posts' : posts,
        #'instagrams' : instagrams,
        #'bookmarks' : bookmarks,
        #'scrobbles' : scrobbles,
        #'tweets' : tweets,
        #'date_list' : date_list
    })
