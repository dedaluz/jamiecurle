from django.conf.urls.defaults import *
from django.contrib import admin
from views import archive, item
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/(?P<slug>[-\w]+)\.html$', item, name='portfolio_item'),
    url(r'^\.html$', archive, name='portfolio'),
)
