from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'featured', 'created', 'tags']
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
