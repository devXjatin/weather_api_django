from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


# login controller
def userLogin(request):
    if request.method == "POST":

        #get username and password
        username = request.POST['username']
        password = request.POST['password']

        #check authentication
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    return render(request,'index.html')

#logout controller
def userLogout(request):
    logout(request)
    return render(request,'index.html')