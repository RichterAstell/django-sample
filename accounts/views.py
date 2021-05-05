from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    print("=== post")
    user = None
    if request.method == "POST":
        member_id = request.POST['member_id']
        password = request.POST['password']
        # print("%d, %s" % (member_id, password))
        print(member_id)
        print(password)
        user = authenticate(request, username=member_id, password=password)
        print(user)

    if user is not None:
        login(request, user)
        return render(request, 'accounts/login_success.html')
    else:
        return render(request, 'accounts/login.html', {'error_message': 'login failed'})
