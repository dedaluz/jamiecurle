from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.TabularInline):
    model = TaggedItem

class TagAdmin2(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        TaggedItemInline
    ]


admin.site.unregister(Tag)
admin.site.register(Tag, TagAdmin2)