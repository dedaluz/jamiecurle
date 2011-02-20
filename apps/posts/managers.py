# -*- coding: utf-8 -*-
from django.db import models

class BlogPostManager(models.Manager):
    
    def for_user(self, user):
        try:
            posts = super(BlogPostManager, self).get_query_set().exclude(status__in=[self.model.DELETED])
        except AttributeError:
            posts = super(BlogPostManager, self).get_query_set().filter(status=self.model.PUBLISHED)
        
        return posts