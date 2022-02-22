from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)


def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)