from django.shortcuts import render
from .models import School, Department, Course

# Create your views here.
def academic(request):
    schools = School.objects.filter()
    departments = Department.objects.filter()
    courses = Course.objects.filter()
    context = {'schools': schools, 'departments': departments, 'courses': courses}
    return render(request, 'academic/academic.html', context)

def course(request, pk):
    courseObj = Course.objects.get(course_name=pk)
    
    pastPaper1_1 = courseObj.pastPaper1_1.all()
    pastPaper1_2 = courseObj.pastPaper1_2.all()
    pastPaper2_1 = courseObj.pastPaper2_1.all()
    pastPaper2_2 = courseObj.pastPaper2_2.all()
    pastPaper3_1 = courseObj.pastPaper3_1.all()
    pastPaper3_2 = courseObj.pastPaper3_2.all()
    pastPaper4_1 = courseObj.pastPaper4_1.all()
    pastPaper4_2 = courseObj.pastPaper4_2.all()
    
    notes1_1 = courseObj.notes1_1.all()
    notes1_2 = courseObj.notes1_2.all()
    notes2_1 = courseObj.notes2_1.all()
    notes2_2 = courseObj.notes2_2.all()
    notes3_1 = courseObj.notes3_1.all()
    notes3_2 = courseObj.notes3_2.all()
    notes4_1 = courseObj.notes4_1.all()
    notes4_2 = courseObj.notes4_2.all()
    
    context = {
        'course': courseObj, 
        'pastPaper1_1': pastPaper1_1, 
        'pastPaper1_2': pastPaper1_2, 
        'pastPaper2_1': pastPaper2_1, 
        'pastPaper2_2': pastPaper2_2,
        'pastPaper3_1': pastPaper3_1, 
        'pastPaper3_2': pastPaper3_2, 
        'pastPaper4_1': pastPaper4_1, 
        'pastPaper4_2': pastPaper4_2,
        'notes1_1': notes1_1, 
        'notes1_2': notes1_2, 
        'notes2_1': notes2_1, 
        'notes2_2': notes2_2,
        'notes3_1': notes3_1, 
        'notes3_2': notes3_2, 
        'notes4_1': notes4_1, 
        'notes4_2': notes4_2,
        }
    
    return render(request, 'academic/course.html', context)


