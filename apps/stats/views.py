# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from models import Spider, Visit



def dashboard(request):
    
    start_date, end_date = Visit.objects.dates()
    
    page_views = Visit.objects.page_views().count()
    unique_visits = Visit.objects.unique_visits().count()
    top_content = Visit.objects.top_content()
    
    return TemplateResponse(request, 'stats/dashboard.html', {
        'unique_visits' : unique_visits,
        'page_views' : page_views,
        'top_content' : top_content,
        'start_date' : start_date, 
        'end_date' : end_date
        
    })

def robots(request):
    disallowed = Spider.objects.filter(disallow=True)
    return TemplateResponse(request, 'stats/robots.txt', {
        'disallowed' : disallowed
    }, mimetype="text/plain")