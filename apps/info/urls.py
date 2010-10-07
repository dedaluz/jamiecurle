from django.conf.urls.defaults import *
from django.contrib import admin
from views import page
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^\.html$', page, name='ultra'),
    url(r'^/(?P<slug>[-\w]+)\.html$', page, name='info_page'),
)
