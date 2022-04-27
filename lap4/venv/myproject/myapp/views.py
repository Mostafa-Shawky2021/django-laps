from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here
def home(request):
    students = Student.objects.all()
    return render(request,'myapp/home.html', {'students':students })

def show(request,std_id):
    std = Student.objects.get(id=std_id) 
    return render(request, 'myapp/show.html',{'student':std})

def delete(request, std_id):
    std = Student.objects.get(id=std_id)
    std.delete()
    return redirect('home')