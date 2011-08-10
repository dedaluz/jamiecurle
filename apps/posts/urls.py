# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import show, create, edit, archive_year, archive_month, index
from feeds import  LatestPostFeed

urlpatterns = patterns('',
    url(r'feed\.rss', LatestPostFeed(), name="feed"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<year>\d{4})/$', archive_year, name="archive_year"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', archive_month, name="archive_month"),
    url(r'^(?P<slug>[\w\-]+)/edit/$', edit, name="edit"),
    url(r'^(?P<slug>[\w\-]+)/$', show, name="show"),
    url(r'$', index, name="index")
)

