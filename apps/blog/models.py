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
    body_class = models.SlugField(blank=True, null=True)
    description = models.TextField()
    content = models.TextField(blank=True)
    html =  models.FilePathField(path="%s/templates/blog/html" % settings.APP_ROOT, recursive=True, blank=True, null=True)
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    comments = models.BooleanField(default=True)
    created = models.DateTimeField()
    images = generic.GenericRelation(Img)
    stylesheets = generic.GenericRelation(Css)
    scripts = generic.GenericRelation(Js)
    tags = TagField()
    related  = models.ManyToManyField('self', blank=True, null=True)
    #
    # poster image
    poster_t = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    poster_s = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    poster_m = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    poster_l = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    poster_f = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    poster_xl = models.ImageField(upload_to='uploads/posters/%Y/%m/%d', blank=True, null=True)
    
    class Meta:
        verbose_name = 'blog'
        ordering = ['featured', '-created']
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {
            'year' : self.created.year,
            'month' : self.created.strftime("%m"),
            'slug' : self.slug
        })
    
    

assets.register(Post)
