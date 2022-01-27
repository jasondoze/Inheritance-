
# establishes the whats to be rendered on the pages when called by the hows accessible through the templates
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .forms import EditorForm, ImageForm, EditImageForm
import random
from django.http import HttpResponseBadRequest



# This function takes in a request and returns the template landingpage.html with an object of all artifacts ordered by their artifact_id. The code is using the objects method to get all artifacts from the database, then it orders them by their artifact_id which will be used later on when rendering the page. The code returns a landingpage.html template that contains the list of all artifacts. 
def landingpage(request):
    artifact = Artifact.objects.all().order_by('artifact_id')
    background = random.choice(artifact)
    return render(request=request, template_name='landingpage.html', context={'background': background, 'id': id}) 

# This function renders the ourstory html  
def ourstory(request):
    return render(request,'ourstory.html')

#This function checks if the request is a GET. If it is, then an artifact object with the given ID will be returned. Next, a form is created that has an imgtitle field and an imgdescr field. The image field of this form contains the image of the artifact. This code will allow the user to edit an artifact by providing a form with the necessary fields.  
def editartifact(request, id):
    if request.method == 'GET':
        artifact = Artifact.objects.get(artifact_id=id)
        form = EditImageForm(instance=artifact) 
        return render(request=request,template_name='editartifact.html', context={'form': form, 'artifact': artifact})
   
    if request.method == 'POST':
        form = EditImageForm(request.POST)
        if form.is_valid():
        
            update_data = {
                'imgdesc': form.cleaned_data['imgdesc'], 
                'imgtitle': form.cleaned_data['imgtitle'],
                'imgfilter': form.cleaned_data['imgfilter'],
                'category': form.cleaned_data['category']
            } 
            Artifact.objects.filter(artifact_id=id).update(**update_data)
            return HttpResponseRedirect(reverse('gallery'))
        else:
            return HttpResponseBadRequest()

# This function starts by creating a list of all the artifacts in the database, then returns a template with an image for each artifact. The code starts by getting all the results from the query that is executed on "Artifact". Then it renders them into a template called gallery.html and renders the gallery.html template with a list of all Artifacts.
def imagedisplay(request):
    resultsdisplay = Artifact.objects.all()
    return render(request, 'gallery.html',{'Artifact':resultsdisplay})

# This function reuses modified version of imagedisplay function to pass request and category as parameters to display image results filtered by category on the gallery page 
def imagecategorydisplay(request, category):
    resultsdisplay = Artifact.objects.filter(category=category)
    return render(request, 'gallery.html',{'Artifact':resultsdisplay})

# This function starts by checking if the request method is POST. If it is, then a form object called ImageForm is created and saved to the database. The instance of this form object is then passed into the template as an argument. The code starts by creating a new instance of ImageForm and saving it to the database with save(). The code is a snippet of code that processes images uploaded by users. If the request method is "POST", then it will process the image and save it to the database.
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'addartifact.html', {'form': form, 'img_obj': img_obj})
            
    else:
        form = ImageForm()
        return render(request, 'addartifact.html', {'form': form})


 # The code starts by getting the artifact_id from the request and then deleting the artifact from the database. Then it returns a HttpResponseRedirect to the addartifact page.
def deleteartifact(request, id):
    # fetch the object related to passed id
    artifact = Artifact.objects.get(artifact_id=id)  
    if request.method =="POST":
        # delete object
        artifact.delete()
        
        return HttpResponseRedirect(reverse('addartifact'))
    else:
        return render(request, 'deleteartifact.html', {'artifact': artifact})
        
   



   