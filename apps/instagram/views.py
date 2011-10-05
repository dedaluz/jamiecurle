# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from models import InstagramPhoto, InstagramComment


def show(request, instagram_id):
    photo = get_object_or_404(InstagramPhoto, pk=instagram_id)
    
    
    return TemplateResponse(request, 'instagram/show.html', {
        'photo' : photo,
    })