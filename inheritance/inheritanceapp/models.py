from django.db import models
from django.db.models.base import *

# Create your models here.
# model(s) for blog-style additions and edits
class Artifact(models.Model):
    artifact_id = models.AutoField(primary_key=True)
    imgtitle = models.CharField(max_length=13)
    imgdesc = models.CharField(max_length=44)
    image=models.ImageField(upload_to='images/')


