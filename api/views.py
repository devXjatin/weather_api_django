from django.shortcuts import render
from requests import request
# Create your views here.


# login controller
def login(request):
    if request.method == "POST":

        #get username and password
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
    return render(request,'index.html')

#logout controller
def logout(request):
    pass