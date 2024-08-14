from django.shortcuts import render
from .models import News
from django.db.models import Q


def news(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(description__icontains=q))
        news = News.objects.filter(multiple_q)
    else:
        news = News.objects.order_by('-time')

    context = {'news': news}
    return render(request, 'news/news.html', context)

