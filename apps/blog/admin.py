from django.contrib import admin
from models import BlogPost, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    list_display= ['title','views', 'description', ]
    list_editable = ['views']
    date_hierarchy = 'created'
    
admin.site.register(BlogPost, BlogPostAdmin)