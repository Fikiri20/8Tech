from django.contrib import admin

# Register your models here.
from .models import Dates, Guidelines, Video, Fee_Structure

admin.site.register(Dates)
admin.site.register(Guidelines)
admin.site.register(Video)
admin.site.register(Fee_Structure)
