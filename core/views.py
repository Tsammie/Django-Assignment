from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    # context = "Welcome to my First Django project, This is the index page"
    # return HttpResponse(context)
    return render(request, 'core/index.html')

def about(request):
    context = {
        "fullname" : "Samuel Oreofe Oritu"
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
      "mail":"Samueloritu2019@gmail.com",
      "number":"07049292634",
      "address":"SQI Iwo road"
    }
    return render(request, 'core/contact.html', context)

def experience(request):
    context = {
        "jobs":"Data Analyst | Django Learner | Problem Solver"
    }
    return render(request, 'core/experience.html', context)

def blog(request):
    return render(request, 'core/blog.html')