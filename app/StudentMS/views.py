from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Git, Leaves, Student
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.contrib.auth import logout


# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        return render(request, "SMS/index.html")
     
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        new_git = Git()
        new_git.name = name
        new_git.email = email
        new_git.message = message
        new_git.save()

    return redirect('index')


@login_required
def student_list(request):
    student_list = Student.objects.all()
    return render(request, "SMS/student_details.html", context={"all_students": student_list})

@login_required
def add_student(request):
    if request.method == "GET":
        return render(request, "SMS/add_student.html")
    if request.method == "POST":
        name = request.POST['student_name']
        roll = request.POST['student_roll']
        regno = request.POST['student_regno']
        age = request.POST['student_age']
        div = request.POST['student_div']
        profile = File(request.FILES.get('profile'))
        

        new_stu = Student()
        new_stu.name = name
        new_stu.roll = roll
        new_stu.regno = regno
        new_stu.age = age
        new_stu.div = div
        new_stu.profile = profile
        new_stu.save()

        return redirect('student_list')

@login_required
def student_delete(request, student_regno):
    student = get_object_or_404(Student, regno=student_regno)
    student.delete()
    return redirect('student_list')


def ap_leaves(request):
    if request.method == "GET":
        return render(request, "SMS/leaves.html")
    if request.method == "POST":
        regno = request.POST['student_regno']
        name=request.POST['student_name']
        reason=request.POST['student_reason']
        student = get_object_or_404(Student, regno = regno)
        
        new_leaves = Leaves(name = name , regno = student, reason = reason)

        new_leaves.save()

        return redirect('login_user')
 
@login_required
def leaves_details(request):
    leaves_list = Leaves.objects.all()
    return render(request, "SMS/leaves_details.html", context={"all_leaves": leaves_list})

@login_required
def manage_leaves(request, leaves_regno):
    
    leaves = Leaves.objects.filter(regno = leaves_regno)
    stu = get_object_or_404(Student, regno = leaves_regno)
    stu.leaves_total += 1
    stu.save()
    leaves.delete()
    return redirect('leaves_details')

@login_required
def disapprove_leaves(request, leaves_regno):
    leaves = Leaves.objects.filter(regno = leaves_regno)
    leaves.delete()
    return redirect('leaves_details')
    
@login_required
def logoutsms(request):
     logout(request)
     return redirect('login_user')
    



