from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return render(request, 'homepage.html')
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def home(request):
    return render(request, 'homepage.html')