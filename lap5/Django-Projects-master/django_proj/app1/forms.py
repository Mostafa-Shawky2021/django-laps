
from django import forms
from .models import Student,Track
from django.contrib.auth.models import User
#auth import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = ('__all__')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname','age','student_track')
        widgets ={
            'fname' : forms.TextInput(attrs={'PlaceHolder': 'Example. Nehal', 'class':'form-control'}),
            'lname' : forms.TextInput(attrs={ 'class':'form-control'}),
            'age' : forms.NumberInput(attrs={ 'class':'form-control'}),
            'Student_track' : forms.Select(attrs={ 'class':'form-control'}),

        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name',)
