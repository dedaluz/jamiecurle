from django.contrib.syndication.views import Feed
from models import BlogPost

class LatestPostFeed(Feed):
    title = "Jamie Curle Posts"
    link = "/"
    description = "The latests posts on Jamie Curler"

    def items(self):
        return BlogPost.objects.filter(status=BlogPost.PUBLISHED).order_by('-created')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description