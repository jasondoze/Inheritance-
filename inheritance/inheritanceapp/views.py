
# establishes the whats to be rendered on the pages when called by the hows accessible through the templates
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .forms import EditorForm, ImageForm


# Create your views here.
def landingpage(request):
   artifact = Artifact.objects.all().order_by('artifact_id')
   return render(request=request, template_name='landingpage.html', context={'artifact': artifact})

def ourstory(request):
    return render(request,'ourstory.html')

def gallery(request):
    return render(request,'gallery.html')

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

def imagedisplay(request):
    resultsdisplay = Artifact.objects.all()
    return render(request, 'gallery.html',{'Artifact':resultsdisplay})

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

    