from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import CAForm

def index(request):
    #return render(request, 'homepage.html')
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def home(request):
    return render(request, 'homepage.html')
def message_test(request):
    return render(request, 'messages.html')
def phone_home_test(request):
    return render(request, 'incentives_phone_layout.html')
def hamburger(request):
    return render(request, 'hamburger_layout.html')
def home_test(request):
    return render(request, 'test_home.html')
def inc_test(request):
    return render(request, 'test_incentives.html')
def resp_test(request):
    return render(request, 'test_responsibility.html')
def layout_test(request):
    return render(request, 'test_layout.html')
def reg_success(request):
    return render(request,'success.html')
def about(request):
    return render(request,'about.html')
def home_view(request):
    context ={}
 
    # create object of form
    form = CAForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect('success')
 
    context['form']= form
    return render(request, "messages.html", context)