from django.db import models



class Spider(models.Model):
    identifier = models.CharField( max_length=255, unique=True)
    
    def __unicode__(self):
        return self.identifier
    
    

class Visit(models.Model):
    http_referer = models.TextField( blank=True, null=True )
    path_info = models.TextField( blank=True, null=True )
    remote_addr = models.IPAddressField( blank=True, null=True )
    is_spider = models.BooleanField(default=False)
    sessionid = models.CharField( max_length=255, blank=True, null=True )
    user_agent = models.CharField( max_length=255, blank=True, null=True )
    created = models.DateTimeField( auto_now_add=True)
    
    def __unicode__(self):
        return u'%s' % self.created
    
    def short_referer(self):
        try:
            return self.http_referer[:100]
        except TypeError:
            return ''
    



class QuerystringParameter(models.Model):
    visit = models.ForeignKey(Visit)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.key
    
