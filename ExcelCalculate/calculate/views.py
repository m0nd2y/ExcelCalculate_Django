from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculate(request) :
    file = request.FILES['fileInput']
    return HttpResponse("calculate, calculate function!")