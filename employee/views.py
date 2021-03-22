from django.shortcuts import render
from django.views import generic
from employee.models import Employee

from django.http import HttpResponse

# Create your views here.
def index():
    return HttpResponse('index page')

def search(request):
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
