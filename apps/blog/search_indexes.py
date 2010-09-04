import datetime
from haystack.indexes import *
from haystack import site
from models import Post


class PostIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    status = CharField(model_attr='status')
    created = DateTimeField(model_attr='created')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Post.objects.filter(status=Post.PUBLISHED)
    
site.register(Post, PostIndex)