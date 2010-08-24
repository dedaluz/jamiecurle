from django.conf import settings
from django.contrib.contenttypes import generic
"""
Heavily inspired by django-mptt

http://code.google.com/p/django-mptt/source/browse/trunk/mptt/__init__.py

"""

registry = []


class BlankImage():
    t = '%s/img/blank.100.100.png' % settings.MEDIA_URL
    s = '%s/img/blank.155.100.png' % settings.MEDIA_URL
    m = '%s/img/blank.240.160.png' % settings.MEDIA_URL
    l = '%s/img/blank.290.240.png' % settings.MEDIA_URL
    f = '%s/img/blank.800.600.png' % settings.MEDIA_URL
    xl = '%s/img/blank.2560.1440.png' % settings.MEDIA_URL
    title = "Placeholder image"
    

class AlreadyRegistered(Exception):
    """
    An attempt was made to register a model for MPTT more than once.
    """
    pass

def register(model):
    """from django.db.models import FieldDoesNotExist, ManyToManyField, ForeignKey
    from models import Js, Css, Img
    # add to registry
    if model in registry:
        raise AlreadyRegistered('The model %s has already been registered.' % model.__name__)
    registry.append(model)
    # Add assets to the model's Options
    opts = model._meta
    # add fields in if they don't exist
    for attr in [(img_attr, Img), (js_attr,Js), (css_attr,Css)]:
        try:
            opts.get_field(attr[0])
        except FieldDoesNotExist:
            # make the related names
            generic.GenericRelation(Img).contribute_to_class(model, img_related_name)
            #tags = generic.GenericRelation(TaggedItem)
            #tags = generic.GenericRelation(TaggedItem)
            #print model, attr[0], attr[1]
            #ForeignKey(attr[1], blank=True, null=True).contribute_to_class(model, attr[0])
            #ForeignKey(model, blank=True, null=True).contribute_to_class(attr[1], attr[0])
            #ManyToManyField(attr[1], blank=True, null=True).contribute_to_class(model, attr[0])
    """
    #
    # now add the shortcuts for images
    model.IMG_CACHE = False
    # a blank image
    model.BLANK_IMAGE = BlankImage()
    # img shortcut
    @property
    def img(self):
        if not self.IMG_CACHE:
            try:
                self.IMG_CACHE = self.images.all()[0]
            except IndexError:
                return self.BLANK_IMAGE
        return self.IMG_CACHE
    
    # sizes of that image
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
    

    model.add_to_class('img', img)
    model.add_to_class('t', t)
    model.add_to_class('s', s)
    model.add_to_class('m', m)
    model.add_to_class('l', l)
    model.add_to_class('f', f)
    model.add_to_class('xl', xl)

