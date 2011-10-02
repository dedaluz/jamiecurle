from django.db import models

class Quote(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    
    def __unicode__(self):
        u'%s' % self.body
    
    