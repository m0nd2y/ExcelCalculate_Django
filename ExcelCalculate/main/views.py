from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from random import *
from .models import *
from sendEmail.views import *
import hashlib

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys() :
        return render(request, 'index.html')
    else :
        return redirect('main_signin')

def signup(request):
    return render(request, 'signup.html')

def join(request):
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    encoded_pw = pw.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
    user = User(user_name = name,  user_password = encrypted_pw, user_email = email)
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

def login(request) :
    loginEmail = request.POST['loginEmail']
    print("loginEmail", loginEmail)
    loginPW = request.POST['loginPW']
    print("loginPW", loginPW)
    try :
        user = User.objects.get(user_email = loginEmail)
    except :
        return redirect('main_loginFail')
    ##login_pw_enc
    encoded_loginPW = loginPW.encode()
    encrypted_loginPW = hashlib.sha256(encoded_loginPW).hexdigest()
    if user.user_password == encrypted_loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else :
        return redirect('main_loginFail')
    
def loginFail(request) :
    return render(request, 'loginFail.html')

def logout(request) :
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')

def verifyCode(request):
    return render(request, 'verifyCode.html')

def verify(request):
    user_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')
    if user_code == cookie_code :
        user = User.objects.get(id = request.COOKIES.get('user_id'))
        user.user_validate = 1
        user.save()
        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        #response.set_cookie('user', user)
        return response
    else:
        redirect('main_verifyCode')

    return redirect('main_index')

def result(request):
    if 'user_name' in request.session.keys() :
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'result.html', content)
    else :
        return redirect('main_signin')