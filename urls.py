from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from apps.utils.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'$^', home, name='home'),
    (r'^admin/', include(admin.site.urls)),
)
