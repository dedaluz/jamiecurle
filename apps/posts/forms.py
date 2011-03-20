# -*- coding: utf-8 -*-
from django import forms
from form_utils.forms import BetterModelForm
from models import BlogPost, BlogImage
from templatetags.posts_tags import render
from apps.utils.widgets import ImageWidget, FileWidget


class BlogImageForm(BetterModelForm):
    src = forms.ImageField(widget=ImageWidget(), label="Image")
    
    class Meta:
        model = BlogImage
    

class BlogPostForm(BetterModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'content', 'slug', 'created', 'status', 'tags']
        fieldsets = [
            ('', {'fields' : ['status', 'title', 'description', 'content', 'tags', ] }),
            ('Optional Info', {'fields' : ['slug', 'created'], 'classes' : ('collapsable', ) }),
        ]
    
    class Media:
        css = {
            'all' : (
                'css/forms.buttons.css',
                'css/forms.css',
                'css/forms.errors.css',
                'css/forms.ordering.css',
                'css/forms.inlinedrag.css',
                'css/forms.tagautocomplete.css',
            )
        }
        js = (  'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.10/jquery-ui.min.js',
                'js/jquery.tools.min.js',
                'js/forms.collapse.js',
                'js/forms.slug.js',
                'js/forms.ordering.js',
                'js/forms.inlinecollapse.js',
                'js/forms.inlinedelete.js',
                'js/forms.inlinedrag.js',
                'js/forms.tagautocomplete.js'
            )
        
    def save(self, commit=True):
        instance = self.instance
        instance.content_rendered = render(instance.content)
        instance = super(BlogPostForm, self).save()
        return instance
    

