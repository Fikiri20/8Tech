from django.contrib import admin
from .models import School, Department, Course, CourseUnit, PastPapers, Notes


# create an inline mode to make adding departments easier


class SchoolsInline(admin.TabularInline):
    model = Department
    extra = 1

class DepartmentInline(admin.TabularInline):
    model = Course
    extra = 1

# class CourseInline(admin.TabularInline):
#     model = CourseUnit
#     extra = 6

# customizing the admin site futher with custom admin layout

class SchoolsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Schools", {"fields": ["school_name"]}),
    ]
    inlines = [SchoolsInline]

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [CourseInline]


# Register your models here.

admin.site.register(School, SchoolsAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course)
admin.site.register(CourseUnit)
admin.site.register(PastPapers)
admin.site.register(Notes)
