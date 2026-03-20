from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    context = "Welcome to my First Django project, This is the index page"
    return HttpResponse(context)