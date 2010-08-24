from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
import tagging
from apps import assets
from apps.assets.models import Img, Css, Js
# Create your models here.

class Book(models.Model):
    READ = 1
    READING = 2
    UNREAD = 3
    MIA = 4
    STATUS_CHOICES = (
        (READ, 'Read'),
        (READING, 'Reading'),
        (UNREAD, 'Unread'),
        (MIA, 'Missing In Action')
    )
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=255, blank=True, null=True)
    #photo = ImageWithThumbsField(upload_to='uploads/books/%Y/%m/%d', sizes=settings.PHOTO_SIZES)
    status = models.SmallIntegerField(choices = STATUS_CHOICES)
    purchased = models.DateField()
    tags = tagging.fields.TagField()
    images = generic.GenericRelation(Img)
    stylesheets = generic.GenericRelation(Css)
    scripts = generic.GenericRelation(Js)
    
    class Meta:
        ordering = ['-purchased']
    
    def __unicode__(self):
        return u'%s' % self.title
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('books_book', (), {
            'year' : self.purchased.year,
            'month' : self.purchased.strftime("%m"),
            'slug' : self.slug
        })
    
    
assets.register(Book)