from django.http.response import HttpResponse
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
    # 이메일 발송 함수 호출
    send_result = send(email, code)
    if send_result :
        return response
    else :
        return HttpResponse("이메일 발송헤 실패했습니다.")
    return response

def signin(request):
    return render(request, 'signin.html')

def verifyCode(request):
    return render(request, 'verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'result.html')