# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from models import Spider

def robots(request):
    disallowed = Spider.objects.filter(disallow=True)
    return TemplateResponse(request, 'stats/robots.txt', {
        'disallowed' : disallowed
    }, mimetype="text/plain")