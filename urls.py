from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', 'django.views.generic.simple.direct_to_template', {'template' : 'home.html'}, name='home'),
    (r'^blog', include('apps.blog.urls')),
    (r'^portfolio', include('apps.portfolio.urls')),
    (r'^admin/', include(admin.site.urls)),
)
