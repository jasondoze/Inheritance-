
from django import forms
from django.forms import widgets
from .models import *

# added editor form to these attributes
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Artifact
        fields = ('artifact_id', 'imgtitle', 'imgdesc', 'image')

class EditorForm(forms.Form):
    imgtitle = forms.CharField(max_length=13, required=True, label=False, widget=forms.TextInput(attrs={'style': 'text-transform:lowercase;', 'placeholder': 'enter title'}))

    imgdesc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'add description'}), label=False, required=True)

    image = forms.URLField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'add image'}))


        