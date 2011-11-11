from django.contrib import admin
from models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ['body', 'twitter_id', 'created']
    search_fields = ['body']

admin.site.register(Tweet, TweetAdmin)