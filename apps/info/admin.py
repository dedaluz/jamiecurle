from django.contrib import admin
from models import Page
from apps.assets.admin import ImgInline, CssInline, JsInline

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','tags']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImgInline, CssInline, JsInline]

admin.site.register(Page, PageAdmin)