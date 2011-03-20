# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
from django.template import Template, Context
from taggit.models import Tag

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
    #data = serializers.serialize('json',tags)
    #return HttpResponse(data)
    t = Template("""[
    {% for tag in tags %}
    { "id": "{{tag.slug}}", "label": "{{tag}}", "value": "{{tag}}" }
    {% if not forloop.last %},{% endif %}
    {% endfor %}]
    """)
    c = Context({'tags': tags})
    r = t.render(c)
    return HttpResponse(r, mimetype="application/json")