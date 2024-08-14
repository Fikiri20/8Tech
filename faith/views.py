from django.shortcuts import render
from .models import Faith
from django.db.models import Q



def faith(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(religion__icontains=q) | Q(short_form__icontains=q))
        faiths = Faith.objects.filter(multiple_q)
    else:
        faiths = Faith.objects.all()
    context = {'faiths': faiths}
    return render(request, 'faith/faith.html', context)
