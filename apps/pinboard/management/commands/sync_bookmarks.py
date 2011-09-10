# -*- coding: utf-8 -*-
from time import mktime
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from apps.instagram.models import InstagramPhoto, InstagramComment
from django.conf import settings
import pinboard
from apps.pinboard.models import PinboardBookmark
from johnny.cache import invalidate
from johnny.middleware import QueryCacheMiddleware


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        p = pinboard.PinboardAccount(settings.PINBOARD_USERNAME, settings.PINBOARD_PASSWORD)
        
        posts = p.posts(count=50)
        
        for post in posts:
            try:
                b  = PinboardBookmark.objects.get(hash=post['hash'])
            except PinboardBookmark.DoesNotExist:
                b = PinboardBookmark()
                b.extended = post['extended']
                b.hash = post['hash']
                b.description = post['description']
                b.url = post['href']
                b.created = datetime.fromtimestamp(mktime(post['time_parsed']))
                b.save()
            
                for tag in post['tags']:
                    b.tags.add(tag)
        
        # now invalidate the cache
        # invalidate the cache
        invalidate(PinboardBookmark)