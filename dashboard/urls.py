from django.urls import path

from . import views


urlpatterns = [
     path("dashboard", views.dashboard, name="dashboard"),
     path("meeting", views.meeting, name="meeting"),
     
     path("assignments", views.assignments, name="assignments"),
     path("quiz", views.quiz, name="quiz"),
     path("exampaper", views.exampaper, name="exampaper"),
     path("notes", views.notes, name="notes"),
     
     path("whats_new", views.whatsnew, name="whats_new"),
     path("feedback", views.feedback, name="feedback"),

     # path("test", views.test, name="test"),
     
     # ======================= basic links end =======================
     
     path("profile",views.profile,name="profile"),
     path("editprofile",views.edit_profile,name="edit_profile"),
     path('update_profile_pic',views.update_profile_pic,name='update_profile_pic'),
     path('update_banner_image',views.update_banner_image,name='update_banner_image'),     
     path('change_password',views.change_password,name='change_password'),
     path("delete_account", views.delete_account, name="delete_account"),
     
     path("submit_assignment/<int:assignment_id>", views.submit_assignment, name="submit_assignment"),
]