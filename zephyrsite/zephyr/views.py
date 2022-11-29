from django.shortcuts import render
from django.http import HttpResponse
from .forms import CAForm

def index(request):
    #return render(request, 'homepage.html')
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def home_view(request):
    context ={}
 
    # create object of form
    form = CAForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "homepage.html", context)