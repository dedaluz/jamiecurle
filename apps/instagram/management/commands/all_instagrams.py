# -*- coding: utf-8 -*-
from time import sleep

from django.core.management.base import BaseCommand, CommandError
from apps.instagram.models import InstagramPhoto, InstagramComment

from django.conf import settings
from instagram import InstagramAPI
from instagram.oauth2 import OAuth2AuthExchangeError


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        # hit instafeed and get the latests, I got the auth token out of instafeed
        api = InstagramAPI(**settings.INSTAGRAM_DEVELOPMENT_CONFIG)
        # delete the current ones
        #InstagramPhoto.objects.all().delete()
        # save this
        # I've got 532 photos so let's loop 19 times in
        max_id = None
        for page in range(19):
            media = api.user_recent_media(count=30, max_id=max_id)
            for ig in media[0]:
                try:
                    instagram = InstagramPhoto.objects.get(instagram_id=ig.id)
                except InstagramPhoto.DoesNotExist:
                    instagram = InstagramPhoto()
                    
                    instagram.caption = ig.caption
                    instagram.instagram_id = ig.id
                    instagram.created = ig.created_time
                    instagram.like_count = ig.like_count
                    instagram.url = ig.link
                    instagram.user_full_name = ig.user.full_name
                    instagram.low_resolution = ig.images['low_resolution'].url
                    instagram.thumbnail = ig.images['thumbnail'].url
                    instagram.standard_resolution = ig.images['standard_resolution'].url
                    try:
                        instagram.latitude = ig.location.point.latitude
                    except AttributeError:
                        pass
                    
                    try:
                        instagram.longitude = ig.location.point.longitude
                    except AttributeError:
                        pass
                    
                    try:
                        instagram.location_id = ig.location.id
                    except AttributeError:
                        pass
                    
                    try:
                        location_name = ig.location.name
                    except AttributeError:
                        pass
                    
                    instagram.save()
                    
                    for comment in ig.comments:
                        try:
                            igc = InstagramComment.objects.get(instagram_id=comment.id)
                        except InstagramComment.DoesNotExist:
                            igc = InstagramComment()
                            igc.instagram_id = comment.id
                            igc.name = comment.user
                            igc.created = comment.created_at
                            igc.comment = comment.text
                            igc.instagramphoto = instagram
                            igc.save()
                            print 'comment %s' % igc.instagram_id
                    
                print ig.id
                max_id = ig.id
            
            sleep(0.5)
        
        