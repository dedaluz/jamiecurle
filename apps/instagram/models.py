from django.db import models


class InstagramPhoto(models.Model):
    caption = models.CharField(max_length=255)
	instagram_id = models.PositiveIntegerField()
	created = models.DateTimeField()
	like_count = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
	url = models.URLField(verify_exists=False)
	user_full_name = models.CharField(max_length=255)
	low_resolution = models.URLField(verify_exists=False)
	thumbnail = models.URLField(verify_exists=False)
	standard_resolution = models.URLField(verify_exists=False)
	latitude = models.DecimalField(max_digits=8, decimal_places=6)
	longitude = models.DecimalField(max_digits=8, decimal_places=6)
	location_id = models.PositiveIntegerField()
	location_name = models.CharField(max_length=255, blank=True, null=True)
    
    
    def __unicode__(self):
        return '<instagram photo: %s>' % self.pk


class InstagramComment(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    comment = models.TextField()
    instagramphoto = models.ForeignKey(InstagramPhoto)
    
    def __unicode__(self):
        return '<instagram comment %s>' % self.name