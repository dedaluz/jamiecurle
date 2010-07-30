from django.db import models
from django.conf import settings
import tagging
from apps.utils.fields import ImageWithThumbsField
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
    photo = ImageWithThumbsField(upload_to='uploads/books/%Y/%m/%d', sizes=settings.PHOTO_SIZES)
    status = models.SmallIntegerField(choices = STATUS_CHOICES)
    purchased = models.DateField()
    tags = tagging.fields.TagField()
    
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
    
    @property
    def t(self):
        try:
            return self.photo.url_100x100
        except AttributeError:
            return False
        
    
    @property
    def s(self):
        try:
            return self.photo.url_155x100
        except AttributeError:
            return False
    
    @property
    def m(self):
        try:
            return self.photo.url_240x160
        except AttributeError:
            return False
    
    @property
    def l(self):
        try:
            return self.photo.url_290x240
        except AttributeError:
            return False
    
    @property
    def f(self):
        try:
            return self.photo.url_800x600
        except AttributeError:
            return False
    
    @property
    def xl(self):
        try:
            return self.photo.url_2560x1440
        except AttributeError:
            return False
    
