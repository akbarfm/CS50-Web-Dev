from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, World!")
def index(request):
    return render(request, 'First_App/index.html')

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse('Hello, David!')

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")
def greet(request, name):
    return render(request, 'First_App/greet.html', {
        "name": name.capitalize()
    })