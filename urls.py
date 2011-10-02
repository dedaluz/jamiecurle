from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponse
from apps.utils.views import index
from apps.blog.feeds import  LatestPostFeed
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'demo', 'django.views.generic.simple.direct_to_template', {'template' : 'demo.html'}),
    (r'^tags/', include('apps.tags.urls', namespace="tags")),
    (r'^posts/', include('apps.blog.urls', namespace="posts")),
    (r'^instagram/', include('apps.instagram.urls', namespace="instagram")),
    (r'^twitter/', include('apps.twitter.urls', namespace="twitter")),
    (r'^authenticate', include('apps.authenticate.urls', namespace="authenticate")),
    (r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
    
    url(r'^$', index, name="home"),
)
