from django.contrib import admin
from models import Visit

class VisitAdmin(admin.ModelAdmin):
    list_display = ['path_info', 'http_referer', 'remote_addr', 'sessionid', 'created']
    

admin.site.register(Visit, VisitAdmin)