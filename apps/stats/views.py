# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from models import Spider, Visit
import datetime



def dashboard(request, start_year=None, start_month=None, start_day=None, end_year=None, end_month=None, end_day=None):
    
    start_date, end_date = Visit.objects.dates()
    
    if (start_year and start_month and start_day):
        start_year = int(start_year)
        start_month =int(start_month)
        start_day = int(start_day)
        start_date = datetime.date(year=start_year, month=start_month, day=start_day)
    
    if (end_year and end_month and end_day):
        end_year = int(end_year)
        end_month =int(end_month)
        end_day = int(end_day)
        end_date = datetime.date(year=end_year, month=end_month, day=end_day)
    
    page_views = Visit.objects.page_views(start_date, end_date).count()
    unique_visits = Visit.objects.unique_visits(start_date, end_date).count()
    top_content = Visit.objects.top_content(start_date, end_date)
    
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