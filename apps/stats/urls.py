# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'$', 'apps.stats.views.dashboard', name="dashboard"),
)

