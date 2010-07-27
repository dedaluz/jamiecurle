from django.conf.urls.defaults import *
from django.contrib import admin
from apps.home.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', home, name='home'),
    (r'^blog', include('apps.blog.urls')),
    (r'^books', include('apps.books.urls')),
    (r'^portfolio', include('apps.portfolio.urls')),
    (r'^admin/', include(admin.site.urls)),
)
