from django.db import models

# Create your models here.

class House(models.Model):
    house_image = models.ImageField(default="default.jpeg")
    house_name = models.CharField(max_length=100)
    house_type = models.CharField(max_length=100, null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    available_rooms = models.IntegerField(default=0)
    houseDetails = models.ManyToManyField('HouseDatails', blank=True)
    phone = models.CharField(max_length=9, default='113631232')
    officials_name = models.CharField(max_length=100, default='8Tech')
    
    def __str__(self):
        return self.house_name
    
class HouseDatails(models.Model):
    name = models.CharField(max_length=100, default='House Images')
    images = models.ImageField(default="default.jpeg")
    
    def __str__(self):
        return self.name

    