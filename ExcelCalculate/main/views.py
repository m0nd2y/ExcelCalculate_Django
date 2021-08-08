from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def join(request):
    print("12341234" + str(request))
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    print("name = " + str(name) + "email = " + str(email) + "pw = " + str(pw))
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()
    return redirect('main_verifyCode')

def signin(request):
    return render(request, 'signin.html')

def verifyCode(request):
    return render(request, 'verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'result.html')