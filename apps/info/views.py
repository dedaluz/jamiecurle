# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import Page


def page(request, slug=None):
    if slug is None:
        slug = 'hello-im-jamie-curle'
        page = get_object_or_404(Page, slug=slug)
        return HttpResponseRedirect(page.get_absolute_url())
    #  get page
    page = get_object_or_404(Page, slug=slug)
    # return
    return render_to_response('info/page.html', RequestContext(request, {
        'page' : page
    }))