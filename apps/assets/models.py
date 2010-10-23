from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer, LEXERS
from pygments.filters import VisibleWhitespaceFilter
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from south.modelsinspector import add_introspection_rules
from tagging.fields import TagField
from apps.utils.fields import ImageWithThumbsField

# Create your models here.

class CodeSnippet(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    title = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    code = models.TextField()
    language = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=10)
    
    class Meta:
        ordering = ['order']
    
    def display(self):
        formatter = HtmlFormatter(cssclass=u'source')
        lexer = get_lexer_by_name(self.language, stripnl=False, stripall=False, encoding='utf-8')
        return mark_safe(highlight(self.code, lexer, formatter) )
    
class Img(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    title = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    src = ImageWithThumbsField(upload_to='uploads/image/%Y/%m/%d', sizes=settings.PHOTO_SIZES)
    order = models.PositiveSmallIntegerField(default=10)
    
    class Meta:
        ordering = ['order']
    
    def __unicode__(self):
        try:
            return u'%s: %s' % (self.title, self.src.path.split('/').pop())
        except ValueError:
            return u'%s' % self.title
    
    @property
    def t(self):
        try:
            return self.src.url_90x96
        except AttributeError:
            return False
        
    
    @property
    def s(self):
        try:
            return self.src.url_140x96
        except AttributeError:
            return False
    
    @property
    def m(self):
        try:
            return self.src.url_240x168
        except AttributeError:
            return False
    
    @property
    def l(self):
        try:
            return self.src.url_290x240
        except AttributeError:
            print 'npwt'
            return False
    
    @property
    def f(self):
        try:
            return self.src.url_800x600
        except AttributeError:
            return False
    
    @property
    def xl(self):
        try:
            return self.src.url_2560x1440
        except AttributeError:
            return False
    

class Attribution(models.Model):
    img = models.OneToOneField(Img)
    license_url = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=255,blank=True, null=True )

class Css(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    path = models.FilePathField(path="%s/templates/assets/css" % settings.APP_ROOT, recursive=True, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=10)
    
    def __unicode__(self):
        return u'%s' % self.path
    
    @property
    def template(self):
        return self.path.replace('%s/templates/' % settings.APP_ROOT, '')
    

class Js(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    path = models.FilePathField(path="%s/templates/assets/js" % settings.APP_ROOT, recursive=True, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=10)
    
    def __unicode__(self):
        return u'%s' % self.path
    
    @property
    def template(self):
        return self.path.replace('%s/templates/' % settings.APP_ROOT, '')
    

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