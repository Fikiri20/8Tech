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

    sections = [
        {'id': 'homepage','year': 1, 'name': '1ST YEAR'},
        {'id': 'about', 'year': 2, 'name': '2ND YEAR'},
        {'id': 'services', 'year': 3, 'name': '3RD YEAR'},
        {'id': 'contact', 'year': 4, 'name': '4TH YEAR'},
    ]



    context = {"courses": courses, "past_papers": past_papers, "notes": notes, "sections": sections, "semester": [1, 2]}
    return render(request, 'academic/course.html', context)





