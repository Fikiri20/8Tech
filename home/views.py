from django.shortcuts import render, redirect
from .models import Scrol, Slide, News, Video




def home(request):
    scroll =Scrol.objects.all()
    slide = Slide.objects.filter()
    news = News.objects.all()
    video = Video.objects.first()
    context = {'slide':slide, 'scroll': scroll, 'news': news, 'video': video}
    return render(request, 'home/index.html', context)


