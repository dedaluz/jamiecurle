# Create your views here.
import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.db.models.query import QuerySet
from tagging.models import Tag, TaggedItem
from apps.books.models import Book
from apps.blog.models import Post
from models import TagProxy

def tags(request, rawtags):
    tagname_list = rawtags.strip('/').split('/')
    tags = Tag.objects.filter(name__in=tagname_list)
    taggeditems = []
    #
    #
    # books
    for obj in TaggedItem.objects.get_intersection_by_model(Book, tags):
        taggeditems.append(
            TagProxy(
                title = obj.title,
                description = obj.description,
                category = 'books',
                t = obj.t,
                s = obj.s,
                m = obj.m,
                l = obj.l,
                f = obj.f,
                xl = obj.xl,
                date = datetime.datetime(year = obj.purchased.year, month = obj.purchased.month, day = obj.purchased.day),
                url = obj.get_absolute_url
            )
        )
    
    for obj in TaggedItem.objects.get_intersection_by_model(Post, tags):
        taggeditems.append(
            TagProxy(
                title = obj.title,
                description = obj.description,
                category = 'blog',
                t = obj.t,
                s = obj.s,
                m = obj.m,
                l = obj.l,
                f = obj.f,
                xl = obj.xl,
                date = obj.created,
                url = obj.get_absolute_url
            )
        )
    taggeditems.sort(key=lambda x: x.date, reverse=True)
    return render_to_response('tags/tags.html', RequestContext(request, {
        'taggeditems' : taggeditems
    }))
