from django.shortcuts import render
from django.http import HttpResponse


def helloWorld(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")

def index(request):
    #return HttpResponse("Hello, world. You're at the money app -> index method")
    return render(request, 'index.html')
