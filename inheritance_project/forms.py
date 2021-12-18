
from django import forms
from .models import *

# added editor form to these attributes
class EditorForm(forms.Form):
    title = forms.CharField(max_length=13, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    img_link = forms.URLField(required=True)
    