from django.contrib import admin
from models import SetTemplate, WorkoutTemplate, Movement

class SetTemplateInline(admin.TabularInline):
    model = SetTemplate
    
class WorkoutTemplateAdmin(admin.ModelAdmin):
    inlines = [SetTemplateInline]

admin.site.register(Movement)
admin.site.register(SetTemplate)
admin.site.register(WorkoutTemplate,  WorkoutTemplateAdmin)