from django.db import models
from taggit.managers import TaggableManager

class InstagramPhoto(models.Model):
    caption = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.PositiveIntegerField()
    created = models.DateTimeField()
    like_count = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    url = models.URLField(verify_exists=False, blank=True, null=True)
    user_full_name = models.CharField(max_length=255)
    low_resolution = models.URLField(verify_exists=False)
    thumbnail = models.URLField(verify_exists=False)
    standard_resolution = models.URLField(verify_exists=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    location_id = models.PositiveIntegerField(blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    
    
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return '<instagram photo: %s>' % self.pk


class InstagramComment(models.Model):
    name = models.CharField(max_length=255)
    instagram_id = models.PositiveIntegerField()
    created = models.DateTimeField()
    comment = models.TextField()
    instagramphoto = models.ForeignKey(InstagramPhoto)
    
    def __unicode__(self):
        return '<instagram comment %s>' % self.name
    
