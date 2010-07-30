from django.db import models

class TagProxy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    t = models.CharField(max_length=255, blank=True)
    s = models.CharField(max_length=255, blank=True)
    m = models.CharField(max_length=255, blank=True)
    l = models.CharField(max_length=255, blank=True)
    f = models.CharField(max_length=255, blank=True)
    xl = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField()
    
    class Meta:
        managed = False