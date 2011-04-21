# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from listeners import create_user_profile

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, editable=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, default=datetime.date.today())
    key = models.CharField(max_length=12)
        
    def __unicode__(self):
        return self.pk
    
    

models.signals.post_save.connect(create_user_profile, sender=User)
    