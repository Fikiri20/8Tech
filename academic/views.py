from django.shortcuts import render
from .models import School, Department, Course, PastPapers, Notes
from django.http import FileResponse, Http404
from django.conf import settings
import os


# Create your views here.

# I modified the academic view to query all the objects instead of
# filter

def academic(request):
    """
    returns the objects from the database model and sends them to the academic.html template"""

    schools = School.objects.all()
    departments = Department.objects.all()
    courses = Course.objects.all()
    context = {'schools': schools, 'departments': departments, 'courses': courses}
    return render(request, 'academic/academic.html', context)



def course(request, pk):
    courses = Course.objects.all()
    past_papers = PastPapers.objects.all()
    notes = Notes.objects.all()
    context = {"courses": courses, "past_papers": past_papers, "notes": notes}
    return render(request, 'academic/course.html', context)





