# -*- coding: utf-8 -*-
from django.db import models

class BlogPostManager(models.Manager):
    
    def for_user(self, user):
    	if user.is_authenticated():
    		posts = super(BlogPostManager, self).get_query_set().all()
    	else:
    		posts = super(BlogPostManager, self).get_query_set().filter(status=self.model.PUBLISHED)

        return posts