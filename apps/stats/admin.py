from django.contrib import admin
from models import Visit

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['sessionid', 'remote_addr']
    date_hierarchy = 'created'
    list_display = ['path_info', 'short_referer', 'user_agent', 'remote_addr', 'sessionid', 'created']
    

admin.site.register(Visit, VisitAdmin)