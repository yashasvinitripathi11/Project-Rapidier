from django.urls import path

from . import views


urlpatterns = [
     path("dashboard", views.dashboard, name="dashboard"),
     path("whatsnew", views.whatsnew, name="whatsnew"),
     path("quiz", views.quiz, name="quiz"),
     path("meeting", views.meeting, name="meeting"),
     path("exampaper", views.exampaper, name="exampaper"),
     path("feedback", views.feedback, name="feedback"),
     path("notes", views.notes, name="notes"),

     path("test", views.test, name="test"),
     
     path("profile",views.profile,name="profile"),
     path("editprofile",views.edit_profile,name="edit_profile"),
]