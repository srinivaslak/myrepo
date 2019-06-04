from django.contrib import admin

from .models import StudentData
class AdminStudentData(admin.ModelAdmin):
    list_display = ['sno','sname','sfee']
admin.site.register(StudentData,AdminStudentData)