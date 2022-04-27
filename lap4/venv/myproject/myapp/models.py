from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Track(models.Model):
    track_name = models.CharField(max_length=20)
    def __str__(self):
        return self.track_name

class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20)
    age   = models.BigIntegerField()
    student_track = models.ForeignKey(Track,on_delete= models.Case)

    def __str__(self):
         return f"{self.fname} {self.lname} {self.age}"


    def is_adult(self):
        return True if self.age > 18 else False 
    
    is_adult_short_description = 'Graduated Student'
    is_adult_boolean = True      

   