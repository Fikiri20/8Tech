from django.db import models

# Create your models here.
class Networking(models.Model):
    item_image = models.ImageField(default="default.jpeg")
    title = models.CharField(max_length=100, default="Adds")
    
    def __str__(self):
        return self.title
    
class Items(models.Model):
    image = models.ImageField(default="default.jpeg")
    title = models.CharField(max_length=100, default='Ads')
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    phone = models.CharField(max_length=9, default='113631232')
    sellers_name = models.CharField(max_length=100, default='8Tech')

    def __str__(self):
        return self.title