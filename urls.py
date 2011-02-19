from django.conf.urls.defaults import *
from django.contrib import admin
from apps.posts.views import index
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^posts/', include('apps.posts.urls', namespace="posts")),
    (r'^authenticate/', include('apps.authenticate.urls', namespace="authenticate")),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="home"),
)
