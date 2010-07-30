from django.conf.urls.defaults import *
from django.contrib import admin
from views import tags

urlpatterns = patterns('',
    url(r'(?P<rawtags>(.*))', tags, name='tags'),
)
