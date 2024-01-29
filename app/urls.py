from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("login-check/", views.login_check, name="login_check"),
    path("register-check/", views.register_check, name="register_check"),
    path("dasbhoard/", views.dasbhoard, name="dasbhoard"),
]