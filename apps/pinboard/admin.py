from django.contrib import admin
from models import PinboardBookmark

class PinboardBookmarkAdmin(admin.ModelAdmin):
    list_display = ['url', 'description', 'created']
    date_hierarchy = 'created'
admin.site.register(PinboardBookmark, PinboardBookmarkAdmin)