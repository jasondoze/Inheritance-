from django.db import models
from django.db.models.base import *
from django.db.models.fields import DateTimeField
# from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# from django.utils import timezone
# now = timezone.now()



# Create your models here.
# model(s) for blog-style additions and edits
# Article model for the database the artifact will be stored in with the following fields:
# artifact_id: primary key for the artifact
# imgtitle: title of the artifact
# imgdesc: description of the artifact
# image: image of the artifact
class Artifact(models.Model):
    artifact_id = models.AutoField(primary_key=True)
    imgtitle = models.CharField(max_length=11)
    imgdesc = models.CharField(max_length=24)
    imgfilter = models.CharField(default="", max_length=500)
    image=models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if not self.your.field:
    #     self.date_field = datetime.datetime.now()
    #     super(ModelName, self).save(*args, **kwargs)

    # _updated = models.DateTimeField()
    # _updatedby = models.ForeignKey(Person, null=True, db_column='_updatedby', blank=True, related_name='acctupdated_by', on_delete=models.SET_NULL)

    class Meta:
       ordering = ['-created_at']

    # def save(self, *args, **kwargs):
        
    #     # open image
    #     pil_img = Image.open(self.image)

    #     # convert the image to array and do some processing
    #     cv_img = np.array(pil_img)
    #     # img = get_filtered_image(cv_img, self.action)
    #     img = get_filtered_image(cv_img, 'ACTION_CHOICES')

    #     # convert back to pil image
    #     im_pil = Image.fromarray(img)

    #     # save
    #     buffer = BytesIO()
    #     im_pil.save(buffer, format='png')
    #     image_png = buffer.getvalue()

    #     self.image.save(str(self.image), ContentFile(image_png), save=False)

    #     super().save(*args, **kwargs)




'''ACTION_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open image
        pil_img = Image.open(self.image)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
'''

