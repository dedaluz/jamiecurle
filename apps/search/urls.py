from django.conf.urls.defaults import *
from views import SearchView


urlpatterns = patterns('haystack.views',
    url(r'^$', SearchView(), name='search'),
)
