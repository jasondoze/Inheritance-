
from django import forms
from django.forms import widgets
from .models import *

# added editor form to these attributes
class EditorForm(forms.Form):
    title = forms.CharField(max_length=13, required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'enter title'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'add description'}), label=False, required=True)

    img_link = forms.URLField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'enter image link'}))
