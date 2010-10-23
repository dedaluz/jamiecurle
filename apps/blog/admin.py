from django.contrib import admin
from models import Post
from apps.assets.admin import ImgInline, CssInline, JsInline,  CodeSnippetInline

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'featured', 'created', 'tags']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImgInline, CssInline, JsInline,  CodeSnippetInline]
    
admin.site.register(Post, PostAdmin)
