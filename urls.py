from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', 'django.views.generic.simple.direct_to_template', {'template' : 'home.html'}, name='home'),
    (r'^admin/', include(admin.site.urls)),
)
