from django.shortcuts import render
from .models import Association
from django.db.models import Q

def association(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(association_name__icontains=q) | Q(short_form__icontains=q))
        associates = Association.objects.filter(multiple_q)
    else:
        associates = Association.objects.all()
    context = {'associates': associates}
    return render(request, 'association/association.html', context)
