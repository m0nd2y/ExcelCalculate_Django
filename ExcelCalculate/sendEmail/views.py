from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def send(request) :
    return HttpResponse("sendEmail, send function!")   
#def send(receiverEmail, verifyCode) :
#    return HttpResponse("sendEmail, send function!")    