from dataclasses import field
from xml.parsers.expat import model
from django.contrib import admin

# Register your models here.
from .models import Student,Track
class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Info', {'fields':['fname','lname','age']}],
        ['Scolarship Info',{'fields':['student_track']}]
    )
    list_display = ('fname', 'lname', 'age', 'student_track','is_adult')
    search_fields=('fname', 'lname', 'student_track__track_name')
    list_filter=('age','student_track__track_name')

class InlineStudent(admin.StackedInline):
    model = Student
    extra=1

class CustomTrack(admin.ModelAdmin):
    inlines=[InlineStudent]

admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)

