from django.db import models
import uuid


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
    past_paper = models.CharField(max_length=50, null=True, blank=True)
    pastPaper1_1 = models.ManyToManyField('PastPaper1_1', blank=True)
    pastPaper1_2 = models.ManyToManyField('PastPaper1_2', blank=True)
    pastPaper2_1 = models.ManyToManyField('PastPaper2_1', blank=True)
    pastPaper2_2 = models.ManyToManyField('PastPaper2_2', blank=True)
    pastPaper3_1 = models.ManyToManyField('PastPaper3_1', blank=True)
    pastPaper3_2 = models.ManyToManyField('PastPaper3_2', blank=True)
    pastPaper4_1 = models.ManyToManyField('PastPaper4_1', blank=True)
    pastPaper4_2 = models.ManyToManyField('PastPaper4_2', blank=True)
    notes1_1 = models.ManyToManyField('Notes1_1', blank=True)
    notes1_2 = models.ManyToManyField('Notes1_2', blank=True)
    notes2_1 = models.ManyToManyField('Notes2_1', blank=True)
    notes2_2 = models.ManyToManyField('Notes2_2', blank=True)
    notes3_1 = models.ManyToManyField('Notes3_1', blank=True)
    notes3_2 = models.ManyToManyField('Notes3_2', blank=True)
    notes4_1 = models.ManyToManyField('Notes4_1', blank=True)
    notes4_2 = models.ManyToManyField('Notes4_2', blank=True)
    
    
    def __str__(self):
        return self.course_name
    
    
class PastPaper1_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class PastPaper1_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.name
    
class PastPaper2_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class PastPaper2_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class PastPaper3_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class PastPaper3_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class PastPaper4_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class PastPaper4_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
    
       
class Notes1_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Notes1_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Notes2_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Notes2_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Notes3_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Notes3_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Notes4_1(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Notes4_2(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name






