from django.contrib import admin
from models import Author, Quote

class AuthorAdmin(admin.ModelAdmin):
    pass


class QuoteAdmin(admin.ModelAdmin):
    pass



#A Dictionary of Scientific Quotations (1991) by Alan L. Mackay, p. 35

admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)