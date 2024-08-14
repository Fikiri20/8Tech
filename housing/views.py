from django.shortcuts import render
from .models import House
from django.db.models import Q



def house(request, pk):
    houseObj = House.objects.get(id=pk)
    houseDetails = houseObj.houseDetails.all()
    context = {'house': houseObj, 'houseDetails': houseDetails}
    return render(request, 'housing/house.html', context)


def housing(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(house_name__icontains=q) | Q(house_type__icontains=q) | Q(rent__icontains=q) | Q(location__icontains=q))
        house = House.objects.filter(multiple_q)
    else:
        house = House.objects.all()
    context = {'house': house}
    return render(request, 'housing/housing.html', context)



