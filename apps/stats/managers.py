from django.db import models
from datetime import datetime


class VisitManager(models.Manager):
    
    def dates(self, start_date=None, end_date=None):
        if start_date is None or end_date is None:
            today = datetime.today()
            year = today.year
            month = today.month
            day = today.day
        
        if start_date is None:
            start_date = datetime(year=year, month=month, day=day, hour=0, minute=0, second=0)
        
        if end_date is None:
            end_date = datetime(year=year, month=month, day=day, hour=23, minute=59, second=59)
        
        return start_date, end_date
    
    
    
    
    
    def top_content(self, start_date=None, end_date=None):
        start_date, end_date = self.dates(start_date, end_date)
        visits = super(VisitManager, self).get_query_set().filter(created__range=(start_date, end_date)).filter(status=self.model.HUMAN)
        visits = visits.values('path_info').annotate(visit_count=models.Count('path_info')).order_by('-visit_count')
        return visits
        
    
    def page_views(self, start_date=None, end_date=None):
        start_date, end_date = self.dates(start_date, end_date)
        return super(VisitManager, self).get_query_set().filter(created__range=(start_date, end_date), status=self.model.HUMAN)
    
    
    
    def unique_visits(self, start_date=None, end_date=None):
        start_date, end_date = self.dates(start_date, end_date)
        
        return super(VisitManager, self).get_query_set().filter(created__range=(start_date, end_date), status=self.model.HUMAN).values('sessionid').distinct()
    
    
    def views_for_path(self, path, start_date=None, end_date=None):
        start_date, end_date = self.dates(start_date, end_date)
        visits = self.page_views(start_date, end_date).filter(path_info=path)
        return visits