# -*- coding: utf-8 -*-
from random import choice


def create_user_profile(sender, instance, **kwargs):
    from apps.users.models import UserProfile
    """ensure that there is always a user profile for users"""
    profile, new = UserProfile.objects.get_or_create(user=instance)
    if new:
        allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWQYZ1234566789890abcdefghjkmnopqrstuvwxyz'
        profile.key = ''.join([choice(allowed_chars) for i in range(12)])
        profile.save()
    
