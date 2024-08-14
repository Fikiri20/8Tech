from django.shortcuts import render
from .models import Networking, Items
from django.db.models import Q

def networking(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(id__icontains=q))
        networks = Networking.objects.filter(multiple_q)
        items = Items.objects.filter(multiple_q)
    else:
        networks = Networking.objects.all()
        items = Items.objects.all()

    context = {'networks': networks, 'items': items}
    return render(request, 'networking/networking.html', context)

