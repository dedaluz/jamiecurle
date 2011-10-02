from django.contrib import admin
from models import Scrobble

class ScrobbleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Scrobble, ScrobbleAdmin)