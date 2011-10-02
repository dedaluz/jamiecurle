from django.db import models
from django.conf import settings


class Scrobble(models.Model):
    name = models.CharField(max_length=255)
    streamable = models.BooleanField(default=True)
    url = models.URLField(verify_exists=False, blank=True, null=True)
    created = models.DateTimeField()
    artist_name = models.CharField(max_length=255)
    artist_url = models.URLField(verify_exists=False, blank=True, null=True)
    artist_mid = models.CharField(max_length=255, blank=True, null=True)
    album_name = models.CharField(max_length=255, blank=True, null=True)
    album_mid = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d/lastfm/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.name
        
    @property
    def img(self):
        try:
            return self.image.url
        except ValueError:
            return '%simg/blank.square.png' % settings.MEDIA_URL
    

    def thumbnail_img(self):
        try:
            return '<img src="%s" width="50" height="50">' % self.image.url
        except:
            return '<img src="%simg/blank.square.png" width="50" height="50">' % settings.MEDIA_URL
    thumbnail_img.short_description = 'Thumb'
    thumbnail_img.allow_tags = True