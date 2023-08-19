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
     path("logout",views.logout,name="logout"),
      path("profile",views.profile,name="profile"),
]