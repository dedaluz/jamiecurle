from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from apps.home.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', home, name='home'),
    #(r'^search/', include('haystack.urls')),
    (r'^404\.html', direct_to_template, {'template' : '404.html'}),
    (r'^500\.html', direct_to_template, {'template' : '500.html'}),
    (r'^search/', include('apps.search.urls')),
    (r'^info', include('apps.info.urls')),
    (r'^tags', include('apps.tags.urls')),
    (r'^blog', include('apps.blog.urls')),
    (r'^books', include('apps.books.urls')),
    (r'^portfolio', include('apps.portfolio.urls')),
    (r'^admin/', include(admin.site.urls)),
)
