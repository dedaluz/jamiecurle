import re
from urllib import unquote
from django.conf import settings
from apps.stats.models import Visit, QuerystringParameter

Q_RE = re.compile('(\&|\?)q\=[\w%\+]+')

class StatsMiddleware(object):
    
    def process_request(self, request):
        try:
            # respect DNT
            if 'HTTP_DNT' in request.META and request.META['HTTP_DNT'] == '1':
                return
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
                # if there was q = get it
                m = re.search(Q_RE, v.http_referer)
                try:
                    q = m.group(0).split('=')
                    terms = q[1]
                    qp = QuerystringParameter()
                    qp.key = 'q'
                    qp.visit = v
                    qp.value = unquote(terms)
                    qp.save()
                except (Exception, IndexError), e:
                    print e
        except:
            pass
    