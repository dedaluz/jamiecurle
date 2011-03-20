# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import tag_search

urlpatterns = patterns('',
    (r'^search/$', tag_search ),
)

