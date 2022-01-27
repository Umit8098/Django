from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

# def student_page(request):
#     return render(request,'student/student.html')

def student_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "number": form.cleaned_data.get('number'),
                "profile_pic": form.cleaned_data.get('profile_pic'),
            }
            # database save process
            # student = Student(first_name=student_name, last_name=student_surname, number=student_number, mentor=student_mentor)
            student = Student(**student_data)
            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            messages.success(request, 'Student added successfully')
            return redirect('student')

    form = StudentForm()
    context = {
        'form': form
    }
    return render(request,'student/student.html', context)
