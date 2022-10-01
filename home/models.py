from platform import mac_ver
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    heading_text = models.CharField(max_length=50)
    description_text = models.TextField()
    color_code = models.CharField(max_length=30, default="#d90769")
    icons = models.CharField(max_length=50, default="bi bi-card-checklist")

    def __str__(self) -> str:
        return self.heading_text  

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    # social media
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")
    linkedin = models.CharField(max_length=200, default="#")
    
    def __str__(self):
        return self.name
