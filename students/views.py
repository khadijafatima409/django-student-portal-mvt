from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.db.models import Q

# Create your views here.



def home(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            Q(full_name__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(request, 'home.html', {'students': students})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            full_name=request.POST.get('full_name'),
            roll_number=request.POST.get('roll_number'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            course=request.POST.get('course'),
            address=request.POST.get('address'),
        )
        return redirect('home')

    return render(request, 'add_student.html')