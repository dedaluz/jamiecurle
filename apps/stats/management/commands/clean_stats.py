# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.stats.models import Visit

pingdom_ips = [u'174.34.162.242', u'70.32.40.2', u'96.31.66.245', u'67.228.213.178', 
u'208.43.68.59', u'94.46.240.121', u'72.46.130.42', u'173.248.147.18', u'173.204.85.217', 
u'212.84.74.156', u'64.141.100.136', u'178.255.152.2', u'64.237.55.3', u'178.255.155.2', 
u'178.255.153.2', u'178.255.154.2', u'69.59.28.19', u'50.23.94.74', u'46.20.45.18', 
u'94.46.4.1', u'108.62.115.226', u'67.205.112.79', u'67.192.120.134', u'207.97.207.200', 
u'207.218.231.170', u'95.211.87.85', u'83.170.113.102', u'74.52.50.50', u'74.53.193.66', 
u'204.152.200.42', u'85.25.176.167', u'174.34.156.130', u'82.103.128.63']

monitor_ips = [u'208.76.245.135', u'188.40.103.239']

google_ips = [u'66.249.71.141', u'66.249.71.106', u'66.249.71.227']


class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        local = Visit.objects.filter(remote_addr__in=settings.STATS_IGNORE_IPS)
        for v in local:
            v.delete()
        
        # delete pingdoms
        pingdoms = Visit.objects.filter(remote_addr__in=pingdom_ips)
        for v in pingdoms:
            v.delete()
        # delete monitor.us
        monitors = Visit.objects.filter(remote_addr__in=monitor_ips)
        for v in monitors:
            v.delete()
            
        

"""
target = Visit.objects.filter(user_agent__icontains='Googlebot')
for v in googles:
    if v.remote_addr not in google_ips:
        google_ips.append(v.remote_addr)
"""