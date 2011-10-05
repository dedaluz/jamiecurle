from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    url(r'^(?P<instagram_id>\d+)\.html$', 'apps.instagram.views.show', name="show"),
)
