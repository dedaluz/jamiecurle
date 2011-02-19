# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import index, post, create

urlpatterns = patterns('',
    url(r'^create/$', create, name="create"),
    url(r'^(?P<slug>[\w+])/$', post, name="view"),
    url(r'^$', index, name="index"),
)

