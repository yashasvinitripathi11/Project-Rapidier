from django.urls import path

from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("signup",views.signup, name="signup"),
    path("dashboard2",views.dashboard2, name="dashboard2"),
    path("invalid",views.invalid, name="invalid")
]

