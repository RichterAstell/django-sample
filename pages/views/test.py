from django.shortcuts import render

# Create your views here.
def test(request):
    print(request.POST.get('user', None))
    pa = request.POST.get('pass', None)
    if (pa == None):
        error_message = "pass is require"
    return render(
        request,
        'pages/test.html',
        {"error_message": error_message}
    )
