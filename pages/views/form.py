from django.shortcuts import render
from ..forms import UserForm

def form(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
    return render(
        request,
        'pages/form.html',
        {"form": form}
    )
