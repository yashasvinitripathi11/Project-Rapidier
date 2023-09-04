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
     path('update_profile_pic',views.update_profile_pic,name='update_profile_pic'),
     path('update_banner_image',views.update_banner_image,name='update_banner_image'),
     
     path('change_password',views.change_password,name='change_password'),
]