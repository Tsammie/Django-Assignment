from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    # context = "Welcome to my First Django project, This is the index page"
    # return HttpResponse(context)
    return render(request, 'core/index.html')

def about(request):
    # myself = {"Name": "Samuel Oreofe Oritu"}
    # return JsonResponse(myself)
    return render(request, 'core/about.html')

def contact(request):
    # details = {"Phone Number": "2347049292634"}
    # return JsonResponse(details)
    return render(request, 'core/contact.html')

def experience(request):
#     me = """ 
# SQI College of ICT
# """
    return render(request, 'core/experience.html')

def blog(request):
    # blog = "Empty"
    # return HttpResponse(blog)
    return render(request, 'core/blog.html')