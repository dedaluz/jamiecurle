# -*- coding: utf-8 -*-
from django import forms
from form_utils.forms import BetterModelForm
from models import BlogPost, BlogImage
from templatetags.posts_tags import render


class BlogImageForm(BetterModelForm):
    
    class Meta:
        model = BlogImage
        
    class Media:
        js = ('js/forms.inlinecollapse.js',)
    
    

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
            'all' : ('css/forms.tagfield.css',)
        }
        js = (  'js/forms.collapse.js',
                'js/forms.slug.js',
                'js/forms.tagfield.js',
                'js/jquery.autocomplete.js',
            )
        
    def save(self, commit=True):
        instance.content_rendered = render(instance.content)
        instance = super(BlogPostForm, self).save()
        return instance
    

