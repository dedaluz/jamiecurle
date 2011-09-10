# -*- coding: utf-8 -*-
import urllib2
from datetime import datetime
from distutils import dir_util
from django.core.management.base import BaseCommand, CommandError
from apps.instagram.models import InstagramPhoto
from django.conf import settings


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        instagrams = InstagramPhoto.objects.filter(img='/meh.jpg')
        for i in instagrams:
            continue
            # sort their paths
            filename = i.standard_resolution.split('/').pop()
            date = i.created.strftime("%Y/%m/%d")
            path = '%suploads/%s/instagram' % (settings.MEDIA_ROOT, date )
            img_path = 'uploads/%s/instagram/%s' % (date, filename)
            thumb_path = 'uploads/%s/instagram/t_%s' % (date, filename)
            # get them
            img = urllib2.urlopen(i.standard_resolution)
            thumb = urllib2.urlopen(i.thumbnail)
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
            i.img = img_path
            i.thumb = thumb_path
            # now save
            i.save()
            print '.'