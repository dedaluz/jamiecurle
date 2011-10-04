from django.contrib import admin
from models import Scrobble

class ScrobbleAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_img', 'artist_name', 'album_name', 'created',]
    date_hierarchy = 'created'
admin.site.register(Scrobble, ScrobbleAdmin)