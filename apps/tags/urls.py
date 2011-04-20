# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import tag_search, tag_list

urlpatterns = patterns('',
    url(r'^(?P<tag>[\w\-]+)/$', tag_list, name="tag_list"),
    (r'^search/$', tag_search ),
)

