from django import forms
from haystack.forms import HighlightedModelSearchForm

class JCHighlightedModelSearchForm(HighlightedModelSearchForm):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder':'I\'m looking for '}))
    