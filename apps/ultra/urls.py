from django.conf.urls.defaults import *
from django.contrib import admin
from views import workout
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^\.html$', workout, name='ultra'),
    #url(r'^/(?P<slug>[-\w]+)\.html$', page, name='info_page'),
)