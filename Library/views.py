from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"landing.html")
def home2(request):
    return HttpResponse("qanday Home2")