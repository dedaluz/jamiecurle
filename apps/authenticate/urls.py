# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import logout_then_login, login
from views import  password_reset_start, password_reset_email, password_reset_choose_new, password_reset_done

urlpatterns = patterns('',
    url(r'^/logout\.html$', logout_then_login, name="logout"),
    url(r'/login\.html$', login, {'template_name': 'authenticate/login.html'}, name="login"),
    url(r'^/zoinks.html$', password_reset_start, name="password_reset"),
    url(r'^/zoinks/email.html$', password_reset_email, name="password_reset_email"),
    url(r'^/zoinks/new.html$', password_reset_choose_new, name="password_reset_choose_new"),
    url(r'^/zoinks/done.html$', password_reset_done, name="password_reset_done"),
)

