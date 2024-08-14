from django.shortcuts import render
from .models import Dates, Guidelines, Video, Fee_Structure


def students(request):
    dates = Dates.objects.all()
    guide = Guidelines.objects.all()
    video = Video.objects.all()
    fee = Fee_Structure.objects.all()

    context = {'dates': dates, 'guide': guide, 'video': video, 'fee': fee}
    return render(request, 'guidelines/students.html', context)


