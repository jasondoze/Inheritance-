
# establishes the whats to be rendered on the pages when called by the hows accessible through the templates
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .forms import EditorForm

# Create your views here.
def landingpage(request):
    artifacts = Artifact.objects.all().order_by('artifact_id')
    return render(request=request, template_name='landingpage.html', context={'artifacts': artifacts})

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
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            img_link = form.cleaned_data['img_link']

            artifacts = Artifact.objects.create(title=title, description=description, img_link=img_link)
        return HttpResponseRedirect(reverse('landingpage'))

def editartifact(request, artifact_id):
    if request.method == 'GET':
        artifact = Artifact.objects.get(pk=artifact_id)
        form = EditorForm(initial={'title': artifact.title, 'description': artifact.description, 'img_link': artifact.img_link })
        return render(request=request, template_name='editartifact.html', context={'form': form, 'artifact_id': artifact_id})

    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                img_link = form.cleaned_data['img_link']
                artifacts = Artifact.objects.filter(pk=artifact_id)
                artifacts.update(title=title, description=description, img_link=img_link)
            elif 'deleteartifact' in request.POST:
                Artifact.objects.filter(pk=artifact_id).delete()
        return HttpResponseRedirect(reverse('landingpage'))


