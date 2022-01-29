
from django import forms
from django.forms import widgets
from .models import *


# This code has the following structure: The first line is the class definition, which defines what kind of object this is. In this case, it's a model form for the Artifact model. The second line is the class Meta definition, which contains information about how to use this class in our application. This includes defining what type of object it represents and its fields (the list of attributes). This code starts with a class definition for the ImageForm. The next line is an import statement that imports the forms module from django-forms. This allows us to use all of the functions in this module to create our form objects. Next we define a Meta class which defines some attributes about our model (Artifact). We also define an attribute called model which will be set to Artifact when we instantiate it later on in our code. We then define a field called imgtitle which is required and must have a value assigned to it before we can save any data into our database table using this form object. Finally, we declare three other fields: imgdesc, image, and artifact_id as being required fields that need values assigned before saving anything into the database table using this form object.

class ImageForm(forms.ModelForm):
    """Form for the image model"""

    imgtitle = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "  enter title", "class": "control-the-form"}))
    imgdesc = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "  enter description", "class": "control-the-form"}))
    image = forms.FileField(label=False, widget=forms.ClearableFileInput(attrs={"class": "control-choosefile-btn"})) 
    class Meta:
        model = Artifact
        fields = ('artifact_id', 'imgtitle', 'imgdesc', 'image', 'category')

# This code is a form for adding an image to the website. The user will enter their title and description, then upload an image from their computer. The code is a form with two fields, one for the title of the image and one for the description.    
class EditorForm(forms.Form):
    imgtitle = forms.CharField(max_length=13, required=True, label=False, widget=forms.TextInput(attrs={'style': 'text-transform:lowercase;', 'placeholder': 'enter title'}))

    imgdesc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'add description'}), label=False, required=True)

    image = forms.URLField(required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'add image'}))


# This code is a form for editing the photo in the website. The user will can re-enter their title and description, then filter their image using sliders located below the photo. The code is a form with three fields, one for the title of the image, one for the description, and one for the filtered image.  
class EditImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Artifact
        fields = ('imgtitle', 'imgdesc', 'imgfilter', 'category')


