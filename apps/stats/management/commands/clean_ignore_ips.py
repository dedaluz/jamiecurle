# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.stats.models import Visit



class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        deletables = Visit.objects.filter(remote_addr__in=settings.STATS_IGNORE_IPS)
        for v in deletables:
            print  v.delete()
        