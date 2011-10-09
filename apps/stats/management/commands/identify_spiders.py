# -*- coding: utf-8 -*-
from time import sleep
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.stats.models import Visit, Spider



class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        spiders = Spider.objects.all()
        
        for spider in spiders:
            visits = Visit.objects.filter(user_agent__icontains=spider.identifier, is_spider=False)
            visits.update(is_spider=True)
        
    

