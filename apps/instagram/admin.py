from django.contrib import admin
from models import InstagramPhoto

class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ['instagram_id', 'thumbnail_img', 'caption', 'created']
    date_hierarchy = 'created'
admin.site.register(InstagramPhoto, InstagramPhotoAdmin)