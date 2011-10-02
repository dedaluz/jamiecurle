from django.conf.urls.defaults import *
from django.contrib import admin
from apps.utils.views import index
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
    url(r'^$', index, name="home"),
)
