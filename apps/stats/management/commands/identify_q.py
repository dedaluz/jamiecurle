# -*- coding: utf-8 -*-
from time import sleep
import re
from django.conf import settings
from django.db import connection
from johnny.cache import invalidate
from django.core.management.base import BaseCommand, CommandError
from apps.stats.models import Visit, QuerystringParameter
from urllib import unquote

Q_RE = re.compile('(\&|\?)q\=[\w%\+]+')

class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        se_visits = Visit.objects.filter(http_referer__icontains='&q=')
        
        QuerystringParameter.objects.all().delete()
        
        for v in se_visits.all():
            m = re.search(Q_RE, v.http_referer)
            try:
                q = m.group(0).split('=')
                terms = q[1]
                qp = QuerystringParameter()
                qp.key = 'q'
                qp.visit = v
                qp.value = unquote(terms)
                qp.save()
            except (Exception, IndexError), e:
                print e
        
        invalidate('stats_querystringparameter', 'stats_spider', 'stats_visit')