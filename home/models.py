from django.db import models
import uuid
    
class Scrol(models.Model):
    scrol_images = models.ImageField(null=True, blank=True, default="default.jpeg", upload_to='static/images')
    topic = models.CharField(max_length=200, default="Latest News")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.topic
    
class Slide(models.Model):
    slide_image = models.ImageField(null=True, blank=True, default="default.jpeg")
    slide_topic = models.CharField(max_length=200, default='Latest News')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.slide_topic
    
class News(models.Model):
    news_images = models.ImageField(null=True, blank=True, default="default.jpeg")
    news_topic = models.CharField(max_length=200,null=True, blank=True)
    news_description = models.TextField(max_length=200,null=True, blank=True)
    news_admin = models.CharField(max_length=100, default="8Tech")
    posted_date = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.news_topic
    
class Video(models.Model):
    caption=models.CharField(max_length=100, default="my video")
    video=models.FileField(upload_to="video/%y")
    news_description = models.TextField(max_length=200,null=True, blank=True)
    news_admin = models.CharField(max_length=100, default="8Tech")
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.caption
    
    
    
    
    
    
