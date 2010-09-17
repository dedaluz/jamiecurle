from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from tagging.fields import TagField
from apps import assets
from apps.assets.models import Img, Css, Js

class Post(models.Model):
    HIDDEN = 1
    DRAFT = 2
    PUBLISHED = 3
        
    STATUS_CHOICES  = (
        (HIDDEN, 'Hidden'),
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body_class = models.SlugField(required=False)
    description = models.TextField()
    content = models.TextField()
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    comments = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    images = generic.GenericRelation(Img)
    stylesheets = generic.GenericRelation(Css)
    scripts = generic.GenericRelation(Js)
    tags = TagField()
    
    class Meta:
        verbose_name = 'blog'
        ordering = ['featured', '-created']
    
    def __unicode__(self):
        return u'%s' % self.pk
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {
            'year' : self.created.year,
            'month' : self.created.strftime("%m"),
            'slug' : self.slug
        })
    
    

assets.register(Post)
