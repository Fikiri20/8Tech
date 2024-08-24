from django.db import models


# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.school_name
    
class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.department_name
    
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    course_name = models.CharField(max_length=200)
    decription = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.course_name


# define models to hold units

class CourseUnit(models.Model):
    course = models.ManyToManyField(Course)
    unit_name = models.CharField(max_length=50)

    def __str__(self):
        return self.unit_name



# let's define a model tha holds past papers

class PastPapers(models.Model):
    past_paper_file = models.FileField(upload_to="past papers")
    unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    name = models.CharField("past paper name", max_length=50)
    year = models.IntegerField(blank=True, null=True)
    sem = models.IntegerField(blank=True, null=True)
    

    class Meta:
        verbose_name_plural = "past papers"

    def __str__(self):
        return self.name

# define a model to store the notes
class Notes(models.Model):
    unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    year = models.IntegerField(blank=True, null=True)
    notes_file = models.FileField(upload_to="notes")
    sem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name



