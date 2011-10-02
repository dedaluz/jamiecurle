from django.contrib import admin
from models import InstagramPhoto

class InstagramPhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(InstagramPhoto, InstagramPhotoAdmin)