from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse

def index():
    return HttpResponse('index pageee')

def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'employee/search.html')
    else:
        error_message = "login failed"
        return render(request, 'employee/login.html', {'error_message': error_message})

def signin2(request):
    return render(request, 'employee/login.html')
