from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Clothes shop")

def about(request):
    return HttpResponse("This is a clothes shop.")