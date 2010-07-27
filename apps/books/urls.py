from django.conf.urls.defaults import *
from django.contrib import admin
from views import blank
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<slug>[-\w]+)\.html$', blank, name='books_book'),
    url(r'^\.html$', blank, name='books'),
)
