from django import forms
from models import *

class WorkoutForm(forms.ModelForm):
    
    class Meta:
        model = Workout