from django.conf.urls.defaults import *
from django.contrib import admin
from apps.home.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', home, name='home'),
    (r'^search/', include('haystack.urls')),
    (r'^info', include('apps.info.urls')),
    (r'^tags', include('apps.tags.urls')),
    (r'^blog', include('apps.blog.urls')),
    (r'^books', include('apps.books.urls')),
    (r'^portfolio', include('apps.portfolio.urls')),
    (r'^admin/', include(admin.site.urls)),
)
