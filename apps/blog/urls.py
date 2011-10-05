# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import show, archive_month, index, edit
from feeds import  LatestPostFeed

urlpatterns = patterns('',
    url(r'feed\.rss', LatestPostFeed(), name="feed"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', archive_month, name="archive_month"),
    url(r'^(?P<slug>[\w\-\+]+)/$', show, name="show"),
    (r'^(?P<slug>[\w\-\+]+)/edit/$', edit),
    #url(r'\.html$', index, name="index")
)

