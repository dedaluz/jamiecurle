# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from apps.blog.models import BlogPost





class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        for post in BlogPost.objects.all():
            post.content = post.content.replace('612x450', '850x600')
            post.save()