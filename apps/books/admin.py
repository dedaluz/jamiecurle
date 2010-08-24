from django.contrib import admin
from models import Book
from apps.assets.admin import ImgInline, CssInline, JsInline

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'purchased', 'tags']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImgInline, CssInline, JsInline]

admin.site.register(Book, BookAdmin)