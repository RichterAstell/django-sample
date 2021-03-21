from django.shortcuts import render
from django.views import generic
from employee.models import Employee

from django.http import HttpResponse

# Create your views here.
def index():
    return HttpResponse('index page')

def search(request):
    if (request.POST.get('first_name') != None and request.POST.get('last_name') != None):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        # list = Employee.objects.filter(
        #     first_name__contains=fname
        #     ,last_name__contains=lname
        # ).order_by('id')[:5]
        list = Employee.objects.filter(
            first_name__contains=fname
        ).filter(
            last_name__contains=lname
        ).order_by('id')[:5]
        return render(request, 'employee/search.html', {'list': list})

    return render(request, 'employee/search.html')

# class SearchView(generic.ListView):
#     template_name = 'employee/search.html'
#     context_object_name = 'list'

#     def get_queryset(self, request):
#         if (request.POST['first_name']):
#             return Employee.objects.filter(
#                 fist_name=request.POST['first_name']
#             ).order_by('id')[:5]

#         return Employee.objects.order_by('id')[:5]
