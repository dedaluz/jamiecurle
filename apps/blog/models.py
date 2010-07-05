from django.db import models
from south.modelsinspector import add_introspection_rules
from apps.utils.fields import ImageWithThumbsField

# Create your models here.




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
    description = models.TextField()
    content = models.TextField()
    status = models.SmallIntegerField(default=DRAFT, choices=STATUS_CHOICES)
    featured = models.BooleanField(default=False)
    comments = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' % self.pk
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {
            'year' : self.created.year,
            'month' : self.created.month,
            'slug' : self.slug
        })
    


class Photo(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    license_url = models.URLField(blank=True, null=True)
    author = models.TextField(max_length=255,blank=True, null=True )
    created = models.DateTimeField(auto_now_add=True)
    photo = ImageWithThumbsField(upload_to='uploads/photo/%Y/%m/%d', sizes=((800,600), (366,240),(155,100),(100,100), ))
    
    def __unicode__(self):
        return u'Photo : %s' % self.pk
    

#
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

