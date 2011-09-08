from django.db import models
from taggit.managers import TaggableManager

class PinboardBookmark(models.Model):
    extended  = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField()
    created = models.DateTimeField()
    shared = models.BooleanField(default=True)
    
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return u'%s' % self.description
    
    