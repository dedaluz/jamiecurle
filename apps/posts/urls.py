# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import index, show, create, edit

urlpatterns = patterns('',
    url(r'^create/$', create, name="create"),
    url(r'^(?P<slug>[\w\-]+)/$', show, name="show"),
    url(r'^(?P<slug>[\w\-]+)/edit/$', edit, name="edit"),
    url(r'^$', index, name="index"),
)

