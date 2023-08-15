from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth



def whatsnew(request):
     return render(request,"whatsnew.html")
def quiz(request):
     return render(request,"quiz.html")
def meeting(request):
     return render(request,"meeting.html")
def exampaper(request):
     return render(request,"exampaper.html")
def feedback(request):
     return render(request,"feedback.html")
def notes(request):
     return render(request,"notes.html")
