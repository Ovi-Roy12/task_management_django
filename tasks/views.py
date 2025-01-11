from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to our Task Management System")

def contact(request):
    return HttpResponse("This is Contact page of Task Management System")

def about(request):
    return HttpResponse("This is the About Page of Task Management System")