from apps.stats.models import Visit
from django.conf import settings

class StatsMiddleware(object):
    
    def process_request(self, request):
        try:
            path = request.META['PATH_INFO']
            ip = request.META['REMOTE_ADDR']
            if  (settings.DEBUG and '/admin/' not in path) or ('/admin/' not in path and ip not in getattr(settings, 'STATS_IGNORE_IPS', []) ):
                v = Visit()
                v.http_referer = request.META.get('HTTP_REFERER', None)
                v.path_info = request.META.get('PATH_INFO', None)
                v.remote_addr = ip
                v.sessionid = request.session.session_key
                v.user_agent = request.META.get('HTTP_USER_AGENT', None)
                v.save()
        except:
            pass
    