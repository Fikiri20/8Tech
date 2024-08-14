from django.shortcuts import render
from .models import Club
from django.db.models import Q


def club(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(club_name__icontains=q) | Q(club_description__icontains=q))
        clubs = Club.objects.filter(multiple_q)
    else:
        clubs = Club.objects.all()
    context = {'clubs': clubs}
    return render(request, 'club/clubs.html', context)
