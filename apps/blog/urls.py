from django.conf.urls.defaults import *
from django.contrib import admin
from views import archive, year, month, post
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<slug>[-\w]+)\.html$', post, name='blog_post'),
    url(r'^/(?P<year>[\d]{4})/(?P<month>[\d]{2})\.html$', month, name='blog_month'),
    url(r'^\.html$', archive, name='blog'),
)
