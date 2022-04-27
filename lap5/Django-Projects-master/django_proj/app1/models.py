from operator import mod
from django.db import models

# Create your models here.
class Track(models.Model):
    track_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.track_name


class Student(models.Model):
    fname= models.CharField(max_length=20,null=True)
    lname= models.CharField(max_length=20,default="noname")
    age= models.IntegerField()
    student_track= models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fname +" "+self.lname
    
    def is_adult(self):
        if self.age >18:
            return True
        else:
            return False
    is_adult.short_description='Graduated Student'
    is_adult.boolean=True