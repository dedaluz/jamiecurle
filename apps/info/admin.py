from django.contrib import admin
from models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','tags']
    prepopulated_fields = {"slug": ("title",)}
    #filter_horizontal = ['images', 'stylesheets', 'scripts']

admin.site.register(Page, PageAdmin)