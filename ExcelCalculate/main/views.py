from django.shortcuts import redirect, render
from random import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def join(request):
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name,  user_password = pw, user_email = email)
    user.save()
    code = randint(1000, 9999)
    response = redirect('main_verifyCode')
    response.set_cookie('code',code)
    response.set_cookie('user_id', user.id)
    return response

def signin(request):
    return render(request, 'signin.html')

def verifyCode(request):
    return render(request, 'verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'result.html')