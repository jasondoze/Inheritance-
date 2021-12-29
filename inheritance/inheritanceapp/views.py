
# establishes the whats to be rendered on the pages when called by the hows accessible through the templates
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .forms import EditorForm, ImageForm


# Create your views here.
# This function takes in a request and returns the template landingpage.html with an object of all artifacts ordered by their artifact_id. The code is using the objects method to get all artifacts from the database, then it orders them by their artifact_id which will be used later on when rendering the page. The code returns a landingpage.html template that contains the list of all artifacts. 
def landingpage(request):
   artifact = Artifact.objects.all().order_by('artifact_id')
   return render(request=request, template_name='landingpage.html', context={'artifact': artifact})

# This function renders the ourstory html  
def ourstory(request):
    return render(request,'ourstory.html')

# This function renders the gallery html file with a list of images.
def gallery(request):
    return render(request,'gallery.html')

# This function is for adding an image to the list of artifacts. The code first checks if the request is a GET or POST, and then it creates a form with all the necessary fields for adding an artifact. If the form is valid, it will create an instance of Artifact and return HttpResponseRedirect(reverse('landingpage') The code will add an image to the database if a form is submitted. If the method of the request is GET, then it will render a template called "addartifact.html" with data from the form in order to return an HTML response. If the method of the request is POST, then it will create an instance of Artifact and assign values to its attributes using cleaned_data from the form.
def addartifact(request):
    if request.method == 'GET':
        form = EditorForm()
        return render(request=request,template_name='addartifact.html', context={'form': form})

    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            imgtitle = form.cleaned_data['imgtitle']
            imgdesc = form.cleaned_data['imgdesc']
            image = form.cleaned_data['image']
            artifact = Artifact.objects.create(imgtitle=imgtitle, imgdesc=imgdesc, image=image)
        return HttpResponseRedirect(reverse('landingpage'))

#This function checks if the request is a GET. If it is, then an artifact object with the given ID will be returned. Next, a form is created that has an imgtitle field and an imgdescr field. The image field of this form contains the image of the artifact. This code will allow the user to edit an artifact by providing a form with the necessary fields.  
def editartifact(request, artifact_id):
    if request.method == 'GET':
        artifact = Artifact.objects.get(pk=artifact_id)
        form = EditorForm(initial={'imgtitle': artifact.imgtitle, 'imgdesc': artifact.imgdescr, 'image': artifact.image })
        return render(request=request, template_name='editartifact.html', context={'form': form, 'artifact_id': artifact_id})

    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                imgtitle = form.cleaned_data['imgtitle']
                imgdesc = form.cleaned_data['imgdesc']
                image = form.cleaned_data['image']
                artifacts = Artifact.objects.filter(pk=artifact_id)
                artifacts.update(imgtitle=imgtitle, imgdesc=imgdesc, image=image)
            elif 'deleteartifact' in request.POST:
                Artifact.objects.filter(pk=artifact_id).delete()
        return HttpResponseRedirect(reverse('landingpage'))

# This function starts by creating a list of all the artifacts in the database, then returns a template with an image for each artifact. The code starts by getting all the results from the query that is executed on "Artifact". Then it renders them into a template called gallery.html and renders the gallery.html template with a list of all Artifacts.
def imagedisplay(request):
    resultsdisplay = Artifact.objects.all()
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

    