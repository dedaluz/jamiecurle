from django.contrib import admin
from models import PinboardBookmark

class PinboardBookmarkAdmin(admin.ModelAdmin):
    pass

admin.site.register(PinboardBookmark, PinboardBookmarkAdmin)