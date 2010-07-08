from django.contrib import admin
from models import Post, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

admin.site.register(Post, PostAdmin)