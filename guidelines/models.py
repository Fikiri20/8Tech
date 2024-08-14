from django.db import models

# Create your models here.

class Dates(models.Model):
    event = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.event 
    
class Guidelines(models.Model):
    guideline = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.guideline 
    
class Video(models.Model):
    caption=models.CharField(max_length=100, default="my video")
    video=models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption
    
    
class Fee_Structure(models.Model):
    name = models.CharField(max_length=100)
    fee = models.ImageField(null=True, blank=True, default="default.jpeg")

    def __str__(self):
        return self.name
    