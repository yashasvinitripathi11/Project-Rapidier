from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def dashboard(request):
     return render(request, "dashboard/dashboard.html")

def whatsnew(request):
     return render(request,"dashboard/whatsnew.html")
def quiz(request):
     return render(request,"dashboard/quiz.html")
def meeting(request):
     return render(request,"dashboard/meeting.html")
def exampaper(request):
     return render(request,"dashboard/exampaper.html")
def feedback(request):
     return render(request,"dashboard/feedback.html")
def notes(request):
     return render(request,"dashboard/notes.html")
