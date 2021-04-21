from django.shortcuts import render

# Create your views here.
def test(request):
    error_message = []
    if request.method == 'POST':
        error_message = __validation(request.POST)
    return render(
        request,
        'pages/test.html',
        {"error_message": error_message}
    )

def __validation(params):
    error_message = []
    # user
    user = params.get('user', None)
    if (len(user) <5):
        error_message.append("the length of the user must be at least 5")
    if (len(user) > 8):
        error_message.append("the length of the user must be less than or equal to 8")
    # password
    password = params.get('password', None)
    if (password == ''):
        error_message.append("password is require")
    return error_message
