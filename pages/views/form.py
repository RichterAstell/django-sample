from django.shortcuts import render
from ..forms import UserForm

def form(request):
    return render(
        request,
        'pages/form.html',
        {"form": UserForm()}
    )
