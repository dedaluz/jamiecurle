from apps.stats.models import Visit

class StatsMiddleware(object):
    
    def process_request(self, request):
        try:
            path = request.META['PATH_INFO']
            if '/admin/' not in path:
                v = Visit()
                v.http_referer = request.META.get('HTTP_REFERER', None)
                v.path_info = request.META.get('PATH_INFO', None)
                v.remote_addr = request.META.get('REMOTE_ADDR', None)
                v.sessionid = request.session.session_key
                v.save()
        except:
            pass
    