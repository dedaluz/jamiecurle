# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from models import * 
from forms import *

def workout(request):
    if request.method == 'POST':
        pass
    
    if request.method == 'GET':
        form = WorkoutForm()
    
    return render_to_response('ultra/workout.html', RequestContext(request, {
        'form' : form
    }))