# -*- coding: utf-8 -*-
import json
import urllib2
from datetime import datetime
from distutils import dir_util
from django.core.management.base import BaseCommand, CommandError
from apps.instagram.models import InstagramPhoto, InstagramComment
from apps.utils.fields import upload_path
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
        #
        # delete some while testing
        #try:
        #    InstagramPhoto.objects.filter(instagram_id__in=['207995726', '203479101', '201843344']).delete()
        #    InstagramComment.objects.get(comment='Just a tree.').delete()
        #except:
        #    pass
        
        # get the latest data
        url = 'http://instafeed.me/f/7ac760.json'
        data = urllib2.urlopen(url)
        feed = json.load(data)
        #iterate over items and create where necessary
        for ig in feed:
            try:
                instagram = InstagramPhoto.objects.get(instagram_id=ig['id'])
            except InstagramPhoto.DoesNotExist:
                
                instagram = InstagramPhoto()
                #instagram.caption = ig['caption']
                instagram.instagram_id = ig['id']
                instagram.created = to_datetime(ig['created_time'])
                instagram.like_count = ig['like_count']
                instagram.url = ig['link']
                instagram.user_full_name = ig['user']
                instagram.low_resolution = ig['images']['low_resolution']
                instagram.thumbnail = ig['images']['thumbnail']
                instagram.standard_resolution = ig['images']['standard_resolution']
                try:
                    lat = ig['location']['latitude']
                    instagram.latitude = lat if len(lat) > 0 else None
                except AttributeError:
                    pass
                #
                try:
                    lng = ig['location']['longitude']
                    instagram.longitude = lat if len(lng) > 0 else None
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
                #
                #
                # suck the images down so we can avoid
                # hitting their bandwidth. I wouldn't like that.
                try:
                    # sort their paths
                    filename = instagram.standard_resolution.split('/').pop()
                    path = '%suploads/%s/instagram' % (settings.MEDIA_ROOT, datetime.today().strftime("%Y/%m/%d") )
                    img_path = 'uploads/%s/instagram/%s' % (datetime.today().strftime("%Y/%m/%d"), filename)
                    thumb_path = 'uploads/%s/instagram/t_%s' % (datetime.today().strftime("%Y/%m/%d"), filename)
                    # get them
                    img = urllib2.urlopen(instagram.standard_resolution)
                    thumb = urllib2.urlopen(instagram.thumbnail)
                    # make the paths
                    dir_util.mkpath(path,mode=0755)
                    # process the image
                    file = open('%s%s' % (settings.MEDIA_ROOT, img_path), 'w')
                    file.write(img.read())
                    file.close()
                    # process the thumb
                    file = open('%s%s' % (settings.MEDIA_ROOT, thumb_path), 'w')
                    file.write(thumb.read())
                    file.close()
                    #
                    instagram.img = img_path
                    instagram.thumb = thumb_path
                    # now save
                    instagram.save()
                except urllib2.HTTPError, e:
                    # abort if there is no photo - this is all about the photos!
                    continue
               
                
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
                
        # invalidate the cache
        invalidate(InstagramPhoto, InstagramComment)
            