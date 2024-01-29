from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate #add this

from django.contrib.auth.models import User # Built-in user model
from django.contrib.auth import login # Built-in login function
from django.contrib.auth import logout # Built-in logout function
from django.contrib.auth.decorators import login_required # for login protected routes
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

@login_required
def dasbhoard(request):
    # get authenticated user
    user = request.user 
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    title = "This is title"
    display_name = user.first_name # "Display Name"
    data = {
        'person_list' : person_list,
        'title' : title,
        'display_name' : display_name,
    }
    return render(
        request, 
        'dashboard.html',
        data
    )

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("dashboard")
    else:
        # No backend authenticated the credentials
        return HttpResponse("credential does not match " + username + ", " + password) #render(request, 'user_management/login.html')
    # person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def register_check(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['display_name']
    
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.save()

    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("dashboard")
    else:
        # No backend authenticated the credentials
        return HttpResponse("register failed :  " + username + ", " + password) #render(request, 'user_management/login.html')
    # person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def logout_page(request):
    logout(request)
    return redirect("index")
