# -*- coding: utf-8 -*-
from time import sleep
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.stats.models import Visit, Spider, Script



class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        spiders = Spider.objects.all()
        
        for spider in spiders:
            visits = Visit.objects.filter(user_agent__icontains=spider.identifier, status=Visit.HUMAN)
            visits.update(status=Visit.SPIDER)
        
        scripts = Script.objects.all()
        for script in scripts:
            visits = Visit.objects.filter(path_info__icontains=script.path, status=Visit.HUMAN)
            visits.update(status=Visit.SCRIPT)
    
