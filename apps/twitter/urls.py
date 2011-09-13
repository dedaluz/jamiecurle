from django.conf.urls.defaults import *
from django.contrib import admin
from views import auth

urlpatterns = patterns('',
    url(r'^$', auth, name="auth"),
)
