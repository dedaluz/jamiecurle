# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.template import Template, Context
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from taggit.models import TaggedItem, Tag


def tag_list(request, tag):
    
    tag = get_object_or_404(Tag, slug=tag)
    qs = TaggedItem.objects.filter(tag=tag)
    
    return TemplateResponse(request, 'tags/tag_list.html', {
        'tagged_objects' : qs,
        'tag' : tag,
    })


def tag_search(request):
    term = request.GET.get('term', False)
    try:
        terms = term.split(',')
        terms.reverse()
        term = terms[0].strip()
        if len(term) > 0:
            tags = Tag.objects.filter(name__istartswith=terms[0].strip())
        else:
            tags = Tag.objects.none()
    except Exception:
        tags = Tag.objects.none()
    t = Template("""[
    {% for tag in tags %}
    { "id": "{{tag.slug}}", "label": "{{tag}}", "value": "{{tag}}" }
    {% if not forloop.last %},{% endif %}
    {% endfor %}]
    """)
    c = Context({'tags': tags})
    r = t.render(c)
    return HttpResponse(r, mimetype="application/json")