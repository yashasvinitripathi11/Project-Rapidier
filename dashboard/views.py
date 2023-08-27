from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from accounts.models import Student
from .models import Feedback


def dashboard(request):
     return render(request, "dashboard/dashboard.html")


def whatsnew(request):
     return render(request, "dashboard/whatsnew.html")


def quiz(request):
     return render(request, "dashboard/quiz.html")


def meeting(request):
     return render(request, "dashboard/meeting.html")


def exampaper(request):
     return render(request, "dashboard/exampaper.html")


def notes(request):
     return render(request, "dashboard/notes.html")


def logout(request):
     auth.logout(request)
     return redirect("signin")


def test(request):
     return render(request, "dashboard/test.html")


def profile(request):
     student = Student.objects.get(id=request.user.id)

     return render(request, "dashboard/profile.html", {"student": student})

# ============================================== Edit Profile ==============================================


def edit_profile(request):

    student = Student.objects.get(id=request.user.id)

    if request.method == "POST":

        student.first_name = request.POST.get("first_name")

        student.last_name = request.POST.get("last_name")

        student.phone_number = request.POST.get("phone_number")

        student.address = request.POST.get("address")

        student.parent_phone_number = request.POST.get("parent_phone_number")

        student.gender = request.POST.get("gender")

        student.bio = request.POST.get("bio")

        student.profile_pic = request.FILES.get("profile_pic")
        student.save()
        return redirect("profile")

    return render(request, "dashboard/edit_profile.html", {"student": student})

# ============================================== Feedback ==============================================


def feedback(request):
     student = Student.objects.get(username=request.user)
     if request.method == 'POST':
          message = request.POST.get('message')
          
          new_feedback = Feedback.objects.create(
               student=student,
               message=message
          )
          
          new_feedback.save()
          
          messages.success(request, 'Thanks for your valuable Feedback!')
          
          return redirect('feedback')
     
     parameters = {
          "student": student
     }
     
     return render(request,'dashboard/feedback.html', parameters)