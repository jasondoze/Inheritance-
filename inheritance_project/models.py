from django.db import models
from django.db.models.base import *

# model(s) for blog-style additions and edits
class Artifact(models.Model):
    artifact_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title = models.CharField(max_length=13)
    description = models.TextField(max_length=444)

