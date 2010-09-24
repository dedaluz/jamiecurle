from django.conf import settings
from django.contrib.contenttypes import generic
"""
Heavily inspired by django-mptt

http://code.google.com/p/django-mptt/source/browse/trunk/mptt/__init__.py

"""

registry = []


class BlankImage():
    t = '%s/img/blank.90.96.png' % settings.MEDIA_URL
    s = '%s/img/blank.140.96.png' % settings.MEDIA_URL
    m = '%s/img/blank.240.168.png' % settings.MEDIA_URL
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
        if self.IMG_CACHE == False:
            try:
                self.IMG_CACHE = self.images.all()[0]
            except IndexError:
                return self.BLANK_IMAGE
        return self.IMG_CACHE

    model.add_to_class('img', img)

