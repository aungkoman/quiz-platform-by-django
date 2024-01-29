from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate #add this

def helloWorld(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")

def index(request):
    #return HttpResponse("Hello, world. You're at the money app -> index method")
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'index.html',{'person_list': person_list, 'title' : 'Person List' })

def login_page(request):
    #return HttpResponse("Hello, world. You're at the money app -> index method")
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'login.html',{'person_list': person_list, 'title' : 'Person List' })

def register_page(request):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'register.html',{'person_list': person_list, 'title' : 'Person List' })

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("user_panel")
    else:
        # No backend authenticated the credentials
        return HttpResponse("credential does not match " + username + ", " + password) #render(request, 'user_management/login.html')
    # person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def register_check(request):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def dasbhoard(request):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })
