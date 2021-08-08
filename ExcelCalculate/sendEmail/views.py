from django.shortcuts import render

# Create your views here.
def send(receiverEmail, verifyCode) :
    return HttpResponse("sendEmail, send function!")    