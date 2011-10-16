# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    
    # dashboard 
    url(r'^/(?P<start_year>\d{4})-(?P<start_month>\d{1,2})-(?P<start_day>\d{1,2})/(?P<end_year>\d{4})-(?P<end_month>\d{1,2})-(?P<end_day>\d{1,2})$', 'apps.stats.views.dashboard', name="dashboard_start_until"),
    url(r'^/(?P<start_year>\d{4})-(?P<start_month>\d{1,2})-(?P<start_day>\d{1,2})$', 'apps.stats.views.dashboard', name="dashboard_from"),    
    url(r'$', 'apps.stats.views.dashboard', name="dashboard"),
)

