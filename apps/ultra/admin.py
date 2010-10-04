from django.contrib import admin
from models import KettlebellWorkout, Exercise, Workout, BarbellSets

class BarbellSetsInline(admin.TabularInline):
    model = BarbellSets

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [BarbellSetsInline]

admin.site.register(KettlebellWorkout)
admin.site.register(Exercise)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(BarbellSets)