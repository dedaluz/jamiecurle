from django.contrib import admin
from models import Visit, Spider, QuerystringParameter

class SpiderAdmin(admin.ModelAdmin):
    list_display=['identifier', 'disallow']
    list_editable=['disallow']

class QuerystringParameterAdmin(admin.ModelAdmin):
    list_display=['key', 'value']
    raw_id_fields = ['visit']

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['sessionid', 'remote_addr', 'user_agent']
    date_hierarchy = 'created'
    list_display = ['created','path_info', 'is_spider',  'search_queries', 'short_user_agent', 'short_referer']
    list_filter = ['is_spider']


admin.site.register(Spider, SpiderAdmin)
admin.site.register(QuerystringParameter, QuerystringParameterAdmin)
admin.site.register(Visit, VisitAdmin)