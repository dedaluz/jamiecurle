from django.db import models
from django.conf import settings
from south.modelsinspector import add_introspection_rules
from tagging.fields import TagField
from apps.utils.fields import ImageWithThumbsField
from apps.assets.models import Img, Css, Js

# Create your models here.


class Post(models.Model):
    IMG_CACHE = False
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
    description = models.TextField()
    stylesheets = models.ManyToManyField(Css, blank=True, null=True,)
    scripts = models.ManyToManyField(Js, blank=True, null=True)
    images = models.ManyToManyField(Img, blank=True, null=True)
    content = models.TextField()
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    comments = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    tags = TagField()
    
    class Meta:
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
    
    
    @property
    def img(self):
        if not self.IMG_CACHE:
            try:
                self.IMG_CACHE = self.images.all()[0]
            except IndexError:
                pass
        return self.IMG_CACHE
    
    @property
    def t(self):
        try:
            return self.img.src.url_100x100
        except AttributeError:
            return False
        
    
    @property
    def s(self):
        try:
            return self.img.src.url_155x100
        except AttributeError:
            return False
    
    @property
    def m(self):
        try:
            return self.img.src.url_240x160
        except AttributeError:
            return False
    
    @property
    def l(self):
        try:
            return self.img.src.url_290x240
        except AttributeError:
            return False
    
    @property
    def f(self):
        try:
            return self.img.src.url_800x600
        except AttributeError:
            return False
    
    @property
    def xl(self):
        try:
            return self.img.src.url_2560x1440
        except AttributeError:
            return False
    

#
# South
rules = [
    (
        (ImageWithThumbsField, ),
        [],
        {
            "blank": ["blank", {"default": True}],
            "max_length": ["max_length", {"default": 100}],
        },
    ),
]
add_introspection_rules(rules, ["^apps\.utils\.fields",])

