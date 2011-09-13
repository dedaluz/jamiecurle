from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.conf import settings

from random import getrandbits
from time import time
from urllib import quote, urlencode
import hmac
from hashlib import sha1


def sig_base(url, method="GET", **kwargs):
  """The signature base."""
  params = ['%s=%s' % (escape(k), escape(kwargs[k])) for k in sorted(kwargs)]
  return '&'.join(map(escape, (method.upper(), url, '&'.join(params))))



def auth(request):
    """
    OAuth oauth_nonce="K7ny27JTpKVsTgdyLdDfmQQWVLERj2zAK5BslRsqyw"
    oauth_callback="http%3A%2F%2Fmyapp.com%3A3005%2Ftwitter%2Fprocess_callback"
    oauth_signature_method="HMAC-SHA1", 
    oauth_timestamp="1300228849",
    oauth_consumer_key="OqEqJeafRSF11jBMStrZz", oauth_signature="Pc%2BMLdv028fxCErFyi8KXFM%2BddU%3D", 
    oauth_version="1.0"
    """
    args = dict(
        oauth_nonce=getrandbits(64),
        oauth_callback = urlencode()'http://127.0.0.1:8000/twitter/callback/'
        oauth_signature_method='HMAC-SHA1',
        oauth_timestamp=int(time()),
        oauth_consumer_key=settings.TWITTER_CONSUMER_KEY,
        oauth_signature
    
    auth_version='1.0',
    
    

    )

    print args
    #get the tokem
    #make the args
    return HttpResponseRedirect('%s')