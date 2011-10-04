from django.db import models

class Visit(models.Model):
    http_referer = models.TextField( blank=True, null=True )
    path_info = models.TextField( blank=True, null=True )
    remote_addr = models.IPAddressField( blank=True, null=True )
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
    

    