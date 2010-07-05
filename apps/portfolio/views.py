# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def item(request, slug):
    return render_to_response('portfolio/item.html', RequestContext(request, { }))
    

def archive(request):
    return render_to_response('portfolio/archive.html', RequestContext(request, { }))
    

