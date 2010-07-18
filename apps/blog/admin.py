from django.contrib import admin
from models import Post, Photo, Script, StyleSheet

class PhotoInline(admin.StackedInline):
    model = Photo
    
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline,]

admin.site.register(Post, PostAdmin)
admin.site.register(StyleSheet)
admin.site.register(Script)