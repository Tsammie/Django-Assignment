from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    context = "Welcome to my First Django project, This is the index page"
    return HttpResponse(context)

def about(request):
    myself = {"Name": "Samuel Oreofe Oritu"}
    return JsonResponse(myself)

def contact(request):
    details = {"Phone Number": "2347049292634"}
    return JsonResponse(details)

def experience(request):
    me = """ 
SQI College of ICT
"""
    return HttpResponse(me)

def blog(request):
    blog = "Empty"
    return HttpResponse(blog)