from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from apps.utils.fields import upload_path, ImageWithThumbsField

class Author(models.Model):
    author = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    photo = ImageWithThumbsField('Image', upload_to=upload_path, sizes=settings.IMAGE_SIZES)
    url = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.author
    
    @models.permalink
    def get_absolute_url(self):
        return('quotes:author', (), {
            'author_slug' : self.slug,
        })

class Quote(models.Model):
    body = models.TextField()
    author = models.ForeignKey(Author)
    source = models.TextField()
    created = models.DateTimeField(blank=True, null=True)
    
    tags = TaggableManager()
    
    def __unicode__(self):
        return u'%s' % self.body
    
    @models.permalink
    def get_absolute_url(self):
        return ( 'quotes:show', (), {
            'author_slug' : self.author.slug,
            'quote_pk' : self.pk,
        })
        
    
    @property
    def title(self):
        return u'%s' % self.author.author
        
    @property
    def description(self):
        return u'%s' % self.body