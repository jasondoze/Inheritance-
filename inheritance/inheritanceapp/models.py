from django.db import models
from django.db.models.base import *
from django.db.models.fields import DateTimeField
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
# model(s) for blog-style additions and edits
# Article model for the database the artifact will be stored in with the following fields:
# artifact_id: primary key for the artifact
# imgtitle: title of the artifact
# imgdesc: description of the artifact
# imgfilter: filter of the artifact
# image: image of the artifact
# created_at: date and time the artifact was created
# updated_at: date and time the artifact was last updated
# category: category of the artifact
class Artifact(models.Model):
    artifact_id = models.AutoField(primary_key=True)
    imgtitle = models.CharField(max_length=13)
    imgdesc = models.CharField(max_length=24)
    imgfilter = models.CharField(default="", max_length=500, blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=25, default="", choices=[
        ('',''),
        ('artistic', 'artistic'),
        ('beautiful', 'beautiful'),
        ('melancholy', 'melancholy'),
        ("profound", "profound")
    ])

    # Meta class orders the photos by the date they were created, with the newest photo first
    class Meta:
       ordering = ['-created_at']


