from django.contrib import admin
from models import Visit, Spider, QuerystringParameter, Script

class ScriptAdmin(admin.ModelAdmin):
    list_display = ['path']

class SpiderAdmin(admin.ModelAdmin):
    list_display=['identifier', 'disallow']
    list_editable=['disallow']

class QuerystringParameterAdmin(admin.ModelAdmin):
    list_display=['key', 'value']
    raw_id_fields = ['visit']

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['sessionid', 'remote_addr', 'user_agent', 'path_info']
    date_hierarchy = 'created'
    list_display = ['created','path_info', 'status',  'search_queries', 'short_user_agent', 'short_referer']
    list_filter = ['status']

admin.site.register(Script, ScriptAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(QuerystringParameter, QuerystringParameterAdmin)
admin.site.register(Visit, VisitAdmin)