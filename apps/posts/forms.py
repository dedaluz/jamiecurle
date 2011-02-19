# -*- coding: utf-8 -*-
from django import forms
from form_utils.forms import BetterModelForm
from models import BlogPost, BlogImage


class BlogImageForm(BetterModelForm):
    
    class Meta:
        model = BlogImage
    

class BlogPostForm(BetterModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'content', 'slug', 'created', 'status']
        fieldsets = [
            ('', {'fields' : ['status', 'title', 'description', 'content'] }),
            ('Optional Info', {'fields' : ['slug', 'created'], 'classes' : ('collapsable', ) }),
        ]
    
