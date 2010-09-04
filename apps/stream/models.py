from django.db import models

# Create your models here.

class Provider(models.Model):
    pass

class Stream(models.Model):
    provider = models.ForeignKey()
    snippet
    created
    thumbnail


class Tumblr

class FlickrPhoto(models.Model):
    pass
    
class LastFMTrack(models.Model):
    pass
    
class TwitterTweet(models.Model):
    pass
