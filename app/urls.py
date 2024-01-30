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
    # Quiz - UI
    path('quiz/', views.quiz_list_page, name='quiz_list_page'),
    path('quiz/detail/<int:quiz_id>/', views.quiz_detail_page, name='quiz_detail_page'),
    path('quiz/create', views.quiz_create_page, name='quiz_create_page'),
    path('quiz/edit/<int:quiz_id>/', views.quiz_edit_page, name='quiz_edit_page'),
    # Quiz - Business Logic
    path('quiz/store/', views.quiz_store, name='quiz_store'),
    path('quiz/update/<int:quiz_id>/', views.quiz_update, name='quiz_update'),
    path('quiz/delete/<int:quiz_id>/', views.quiz_delete, name='quiz_delete'),
    # Questions - UI
    path('question/create/', views.question_create_page, name='question_create_page'),
    path('question/detail/<int:question_id>/', views.question_detail_page, name='question_detail_page'),
    path('question/edit/<int:question_id>/', views.question_edit_page, name='question_edit_page'),
    # Questions - Business Logic
    path('question/store/', views.question_store, name='question_store'),
    path('question/update/<int:question_id>/', views.question_update, name='question_update'),
]