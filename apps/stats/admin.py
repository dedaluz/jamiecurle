from django.contrib import admin
from models import Visit, Spider, QuerystringParameter

class QuerystringParameterAdmin(admin.ModelAdmin):
    list_display=['key', 'value']

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['sessionid', 'remote_addr']
    date_hierarchy = 'created'
    list_display = ['path_info', 'is_spider', 'user_agent', 'http_referer']
    list_filter = ['is_spider']


admin.site.register(Spider)
admin.site.register(QuerystringParameter, QuerystringParameterAdmin)
admin.site.register(Visit, VisitAdmin)