# -*- coding: utf-8 -*-
from django.contrib.auth.models import User



class CustomUserBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    
    def authenticate(self, username=None, password=None):
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        # now check the password
        if user.check_password(password):
                    return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    

