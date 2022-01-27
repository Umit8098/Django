from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

# def student_page(request):
#     return render(request,'student/student.html')

def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect('student')
    context = {
        'form': form
    }
    return render(request,'student/student.html', context)
