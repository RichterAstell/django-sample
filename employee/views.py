from django.shortcuts import render
from django.views import generic
from employee.models import Employee

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SearchView(generic.ListView):
    template_name = 'employee/search.html'
    context_object_name = 'list'

    def get_queryset(request):
        return Employee.objects.order_by('id')[:5]
