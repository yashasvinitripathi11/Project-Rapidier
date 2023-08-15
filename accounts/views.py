from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student


def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard2")
        
        else:
            return redirect("invalid")

    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        bio = request.POST.get("bio")
        phone_number = request.POST.get("phone_number")
        parent_phone_number = request.POST.get("parent_phone_number")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        profile_pic = request.POST.get("profile_pic")

        new_user = Student.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio = bio,
            phone_number = phone_number, 
            parent_phone_number = parent_phone_number,
            address = address,
            gender = gender,
            profile_pic = profile_pic
        )

        new_user.set_password(password)

        new_user.save()

        return redirect("dashboard2")
        

    return render(request,"signup.html")
def dashboard2(request):
    
    user = request.user

    parameters = {
        "user":user
    }
    return render(request,"dashboard.html",parameters)

def invalid(request):
    return render(request,"invalid.html")




