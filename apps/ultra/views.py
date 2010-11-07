# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from forms import WorkoutForm, SetForm
from models import Workout, Set, WorkoutTemplate

def workout(request):
    template = WorkoutTemplate.objects.get(pk=3)
    
    if request.method == 'POST':
        workoutform = WorkoutForm(request.POST)
        print request.POST
        #setform = SetForm(request.POST)
    if request.method == 'GET':
        #
        #
        #
        workoutform = WorkoutForm()
        setforms = []
        # set forms for each of the sets in the template
        for i, wo_set in enumerate(template.settemplate_set.all()):
            initial = {
                'movement' : wo_set.movement.pk,
                'total' : wo_set.total,
                'reps' : wo_set.reps,
            }
            prefix = 'wo_set_%s' % i
            # append the form to the wo_sets
            setforms.append(SetForm(initial=initial, prefix=prefix))
        #setform = SetForm()
    
    return render_to_response('ultra/workout.html', RequestContext(request, {
        'workoutform' : workoutform,
        'setforms' : setforms
        #'form' : form
    }))