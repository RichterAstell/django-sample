from django.shortcuts import render
from django.views import generic
from employee.models import Employee

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .login import LoginForm

from django.http import HttpResponse

import logging
from django.contrib.auth import authenticate, login, logout

from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
logger.info("log info test!")

# Create your views here.
def index():
    return HttpResponse('index page')


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

def signout(request):
    logout(request)
    return render(request, 'employee/login.html')

# class Login(LoginView):
#     """Login page"""
#     form_class = LoginForm
#     template_name = 'employee/login.html'
#     def get(self, request):
#         return render(request, 'employee/login.html')

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'employee/search.html')
#         else:
#             error_message = "login failed"
#             return render(request, 'employee/login.html', {'error_message': error_message})

# login = Login.as_view()

# def login(request):
#     return render(request, 'employee/login.html')

@login_required
def search(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    e = Employee.objects
    if (request.POST.get('first_name') != None):
        fname = request.POST.get('first_name')
        e = e.filter(first_name__contains=fname)
    if (request.POST.get('last_name') != None):
        lname = request.POST.get('last_name')
        e = e.filter(last_name__contains=lname)

    list = e.order_by('id')[:5]
    return render(request, 'employee/search.html', {'list': list})

    # return render(request, 'employee/search.html')

# class SearchView(generic.ListView):
#     template_name = 'employee/search.html'
#     context_object_name = 'list'

#     def get_queryset(self, request):
#         if (request.POST['first_name']):
#             return Employee.objects.filter(
#                 fist_name=request.POST['first_name']
#             ).order_by('id')[:5]

#         return Employee.objects.order_by('id')[:5]
