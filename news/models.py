from django.db import models


class News(models.Model):
    image = models.ImageField(default='default,jpeg')
    title = models.CharField(max_length=200)
    admin_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
