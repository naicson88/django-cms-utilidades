from django.db import models

from cms.models import CMSPlugin


class ActivitieModel(CMSPlugin):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
       return self.title + " - Image"
   

# Create your models here.
class ActivitiesPanelModel(CMSPlugin):
    title = models.CharField(max_length=30)
    image = models.ForeignKey(ActivitieModel, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

