from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student, Subject


def signin(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        
        else:
            return redirect("signin")

    return render(request,"accounts/signin.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email=request.POST.get("email")
        password = request.POST.get("password")
        subject = request.POST.get("subject")


        new_user = Student.objects.create(
            username=username,
            first_name=first_name,
            last_name = last_name,
            email=email           
        )
        
        new_user.subjects.add(subject)

        new_user.set_password(password)

        new_user.save()

        return redirect("signin")
    
    parameters = {
        "subjects": Subject.objects.all()
    }
    
    return render(request,"accounts/signup.html", parameters)

# =================================== logout ============================

def logout(request):
     auth.logout(request)
     return redirect("home")



