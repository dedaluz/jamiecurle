from django import forms
from django.forms.models import inlineformset_factory
from models import Workout, Set




class WorkoutForm(forms.ModelForm):
    
    class Meta:
        model = Workout
    

class SetForm(forms.ModelForm):
    
    class Meta:
        model = Set
    
