from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Post

class LatestPostFeed(Feed):
    title = "jamiecurle.com Blog Posts"
    link = '/blog.html'
    description = "Blog posts from jamiecurle.com"
    
    def items(self):
        return Post.objects.filter(status=Post.PUBLISHED)
        
    def item_title(self, item):
        return item.title
        
    def item_description(self, item):
        return item.description
        
    def item_pubdate(self,item):
        return item.created