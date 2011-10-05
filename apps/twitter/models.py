from django.db import models
from taggit.managers import TaggableManager

class Tweet(models.Model):
    twitter_id = models.BigIntegerField()
    created = models.DateTimeField()
    body = models.TextField()
    is_favourite = models.BooleanField( default=False )
    reply_to_status_id = models.BigIntegerField( blank=True, null=True )
    reply_to_user_id = models.BigIntegerField( blank=True, null=True )
    reply_to_user_name = models.CharField( max_length=255, blank=True, null=True )
    retweet_count = models.PositiveIntegerField( default=0, blank=True, null=True )
    
    tags = TaggableManager()
    
    def description(self):
        return self.body
    
    def get_absolute_url(self):
        return 'https://twitter.com/#!/jamiecurle/status/%s' % self.twitter_id
    
    class Meta:
        ordering = ['-created']
    
    def __unicode__(self):
        return '%s' % self.twitter_id
    
    
    