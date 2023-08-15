from django.urls import path

from . import views


urlpatterns = [
     path("whatsnew", views.whatsnew, name="whatsnew"),
     path("quiz", views.quiz, name="quiz"),
     path("meeting", views.meeting, name="meeting"),
     path("exampaper", views.exampaper, name="exampaper"),
     path("feedback", views.feedback, name="feedback"),
     path("notes", views.notes, name="notes"),
 
 
]    