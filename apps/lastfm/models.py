from django.db import models
from django.conf import settings


class Scrobble(models.Model):
    name = models.CharField(max_length=255)
    streamable = models.BooleanField(default=True)
    url = models.URLField(verify_exists=False, blank=True, null=True)
    played_on = models.DateTimeField()
    artist_name = models.CharField(max_length=255)
    artist_url = models.URLField(verify_exists=False, blank=True, null=True)
    artist_mid = models.CharField(max_length=255, blank=True, null=True)
    album_name = models.CharField(max_length=255, blank=True, null=True)
    album_mid = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d/lastfm/', blank=True, null=True)
    
    class Meta:
        ordering = ['-played_on']
    
    def __unicode__(self):
        return u'%s' % self.name
        
    @property
    def img(self):
        try:
            return self.image.url
        except ValueError:
            return '%simages/blank.square.png' % settings.MEDIA_URL
    

