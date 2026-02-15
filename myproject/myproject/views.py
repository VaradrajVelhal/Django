from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, World, you are at the about page.")


def contact(request):
    return HttpResponse("Hello, World, you are at the contact page.")
