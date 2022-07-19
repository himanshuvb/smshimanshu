from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from StudentMS.models import Student

def login_user(request):
        if request.method == "GET":
            return render(request, "SMS/login.html")
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index') 
                else:
                    return render(request, "SMS/login.html", context={"error": "User is not active"})
            else:
                return render(request, "SMS/login.html", context={"error": "Login credentials are incorrect"})

def student_login(request):
    if request.method == "GET":
        return render(request, "SMS/stu_login.html")
    if request.method == "POST":
         name = request.POST['name']
         regno = request.POST['regno']
         student = get_object_or_404(Student,name=name,regno = regno)
        
         if student is not None:
                if student:
                    return redirect('ap_leaves')
                else:
                    return render(request, "SMS/stu_login.html", context={"error": "User is not active"})
         else:
            return render(request, "SMS/stu_login.html", context={"error": "Login credentials are incorrect"})
