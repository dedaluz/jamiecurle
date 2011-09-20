# -*- coding: utf-8 -*-
import urllib2
import sys
import datetime
import os
from time import sleep, mktime
from distutils import dir_util
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.lastfm.models import Scrobble
from lxml import etree



class Command(BaseCommand):
    #processed = 0
    #startpage = 68
    #endpage = 69
    limit = 50
    
    
    def handle(self, *args, **kwargs):
        # delete all
        #Scrobble.objects.all().delete()
        # get the first bactch
        #print 'fetching page %s' % page
        #url =' http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=jamiecURLe&limit=%s&api_key=%s&page=%s' % (self.limit, settings.LASTFM_KEY, page)
        # get the last scrobble
        last_scrobble = Scrobble.objects.all()[:1][0]
        timefrom = mktime(last_scrobble.created.timetuple())
        print "syncing new scrobbles"
        url =' http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=jamiecURLe&limit=%s&api_key=%s&from=%s' % (self.limit, settings.LASTFM_KEY, timefrom)
        request = urllib2.urlopen(url)
        raw = request.read()
        scrobbles = etree.fromstring(raw)
        
        for xmldata in scrobbles.iter('track'):
            # create the scrobble
            scrobble = self.create_scrobble(xmldata)
            # feedback
            sys.stdout.write('.')
            sys.stdout.flush()
            
            # be nice - wait a second
            #print ''
            #print 'sleeping to be nice to the API'
            #sleep(1)
        # wrap up with a summary
        
    
    
    def create_scrobble(self, xmldata):
        
        if xmldata.get('nowplaying') =='true':
            return
            
        created = datetime.datetime.fromtimestamp( float( xmldata[10].get('uts') ) )
        
        try:
            s = Scrobble.objects.get(created=created, name=xmldata[1].text)
        except Scrobble.DoesNotExist:
            s = Scrobble()
            # artist info
            s.artist_name = xmldata[0].text
            s.artist_mid = xmldata[0].get('mbid')
    
            # album info
            s.album_name = xmldata[4].text
            s.album_mid = xmldata[4].get('mbid')
    
            # track info
            s.streamable = True if xmldata[2].text == '1' else False
            s.name = xmldata[1].text
            s.created = created
            s.url = xmldata[5].text
    
    
            # image
            img = xmldata[9].text
            try:
                filename = img.split('/').pop()
                date = s.created.strftime("%Y/%m/%d")
                path = '%suploads/%s/lastfm' % (settings.MEDIA_ROOT, date )
                img_path = 'uploads/%s/lastfm/%s' % (date, filename)
                try:
                    img = urllib2.urlopen(img)
                    # make the paths
                    dir_util.mkpath(path,mode=0755)
                    # process the image
                    f = open('%s%s' % (settings.MEDIA_ROOT, img_path), 'w')
                    f.write(img.read())
                    f.close()
                    #
                    s.image = img_path
                    f.close()
                except (urllib2.HTTPError, AttributeError, urllib2.URLError):
                    pass
            except AttributeError:
                pass    
            
            # save and increment
            s.save()
        return s
"""
import lastfm
import urllib2
import sys
import datetime
import os
from distutils import dir_util
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.lastfm.models import Scrobble

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        # delete a;;
        Scrobble.objects.all().delete()
        
        api = lastfm.Api(settings.LASTFM_KEY)
        user = api.get_user('jamiecURLe')
        tracks = user.get_recent_tracks()
        for track in tracks:
            try:
                s = Scrobble.objects.get(created=track.created)
            except Scrobble.DoesNotExist:
                s = Scrobble()
                s.name = track.name
                s.streamable = track.streamable
                s.url =  track.url
                s.created = track.created
                s.artist_name = track.artist.name
                s.album_name = track.album.name
                s.album_mid = track.album.mbid
                
                if track.image.get('extralarge', False):
                    img = track.image['extralarge']
                    filename = track.image['extralarge'].split('/').pop()
                    date = s.created.strftime("%Y/%m/%d")
                    path = '%suploads/%s/lastfm' % (settings.MEDIA_ROOT, date )
                    img_path = 'uploads/%s/lastfm/%s' % (date, filename)
                    if not os.path.exists('%s%s' % (settings.MEDIA_ROOT, img_path)):
                        try:
                            img = urllib2.urlopen(img)

                            # make the paths
                            dir_util.mkpath(path,mode=0755)
                            # process the image
                            f = open('%s%s' % (settings.MEDIA_ROOT, img_path), 'w')
                            f.write(img.read())
                            f.close()
                            #
                            s.image = img_path
                            f.close()
                        except (urllib2.HTTPError, AttributeError, urllib2.URLError):
                            pass
                s.save()
            sys.stdout.write('.')
            sys.stdout.flush()
            

"""