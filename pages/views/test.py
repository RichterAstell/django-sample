from django.shortcuts import render

# Create your views here.
def test(request):
    print(request.POST.get('user', None))
    print(request.POST.get('pass', None))
    return render(
        request,
        'pages/test.html',
    )
