# -*- coding: utf-8 -*-
import json
import urllib2
from django.core.management.base import BaseCommand, CommandError
from apps.instagram.models import InstagramPhoto, InstagramComment
from django.conf import settings
from johnny.cache import invalidate
from johnny.middleware import QueryCacheMiddleware



def to_datetime(d):
    d = d.split(',')
    d = d[1].split('+')
    d = d[0]
    d = d.split(' ')
    #d = d.replace(' Jan ', '-1-')
    d[2] = d[2].replace('Jan', '01')
    d[2] = d[2].replace('Feb', '02')
    d[2] = d[2].replace('Mar', '03')
    d[2] = d[2].replace('Apr', '04')
    d[2] = d[2].replace('May', '05')
    d[2] = d[2].replace('Jun', '06')
    d[2] = d[2].replace('Jul', '07')
    d[2] = d[2].replace('Aug', '08')
    d[2] = d[2].replace('Sep', '09')
    d[2] = d[2].replace('Oct', '10')
    d[2] = d[2].replace('Nov', '11')
    d[2] = d[2].replace('Dec', '12')
    
    d = '%s-%s-%.2d %s' % (d[3], d[2], int(d[1]), d[4])
    return d

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        # hit instafeed and get the latests
        #api = InstagramAPI(**settings.INSTAGRAM_DEVELOPMENT_CONFIG)
        #media = api.user_recent_media(count=30)
        
        
        ip = InstagramPhoto.objects.filter(instagram_id__in=[201843344, 203479101])
        ip.delete()
        
        #feed = 'http://instafeed.me/f/7ac760.json'
        url = 'http://192.168.1.13:8001/f/7ac760.json'
        data = urllib2.urlopen(url)
        feed = json.load(data)
        
        for ig in feed:
            
            try:
                instagram = InstagramPhoto.objects.get(instagram_id=ig['id'])
            except InstagramPhoto.DoesNotExist:
                print 'HIT %s' % ig['id']
                

                instagram = InstagramPhoto()
                
                instagram.caption = ig['caption']
                instagram.instagram_id = ig['id']
                instagram.created = to_datetime(ig['created_time'])
                instagram.like_count = ig['like_count']
                instagram.url = ig['link']
                instagram.user_full_name = ig['user']
                instagram.low_resolution = ig['images']['low_resolution']
                instagram.thumbnail = ig['images']['thumbnail']
                instagram.standard_resolution = ig['images']['standard_resolution']
                try:
                    instagram.latitude = ig['location']['latitude']
                except AttributeError:
                    pass
                #
                try:
                    instagram.longitude = ig['location']['longitude']
                except AttributeError:
                    pass
                #
                try:
                    lid = int(ig['location']['id'])
                    instagram.location_id = ig['location']['id']
                except ValueError:
                    pass
                
                try:
                    location_name = ig['location']['name']
                except AttributeError:
                    pass
                
                instagram.save()
                
                for comment in ig['comments']:
                    try:
                        igc = InstagramComment.objects.get(instagram_id=comment['id'])
                    except InstagramComment.DoesNotExist:
                        igc = InstagramComment()
                        igc.instagram_id = comment['id']
                        igc.name = comment['name']
                        igc.created =  to_datetime(comment['created_at'])
                        igc.comment = comment['text']
                        igc.instagramphoto = instagram
                        igc.save()
                        print 'comment %s' % igc.instagram_id
                
        # invalidate the cache
        invalidate(InstagramPhoto, InstagramComment)
            