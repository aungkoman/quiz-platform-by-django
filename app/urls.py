from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("login-check/", views.login_check, name="login_check"),
    path("register-check/", views.register_check, name="register_check"),
    # path("dasbhoard/", views.dasbhoard, name="dasbhoard"),
    path('dashboard/', views.dasbhoard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
    path('quiz/', views.quiz_list_page, name='quiz_list_page')
]