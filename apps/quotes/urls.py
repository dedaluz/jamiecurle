# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import show, index, author

urlpatterns = patterns('',
    url(r'^/(?P<author_slug>[\w\-]+)/(?P<quote_pk>\d+)\.html$', show, name="show"),
    url(r'^/(?P<author_slug>[\w\-]+)\.html$', author, name="author"),    
    url(r'^\.html$', index, name="index"),
)

