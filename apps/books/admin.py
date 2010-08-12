from django.contrib import admin
from models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'purchased', 'tags']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ['images', 'stylesheets', 'scripts']

admin.site.register(Book, BookAdmin)