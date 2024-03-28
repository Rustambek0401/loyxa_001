from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("SALOM USERS1")
def index2(request):
    return HttpResponse("SALOM USERS2")

# Create your views here.
