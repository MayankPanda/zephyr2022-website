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
def help_page(request):
    return render(request,'faq.html')
def main_homepage(request):
    return render(request,'main_homepage.html')
def surgical_strike(request):
    return render(request,'surgical_strike.html')
def water_rocket(request):
    return render(request,'water_rocket.html')
def aerocontraption(request):
    return render(request,'aerocontraption.html')
def button_test(request):
    return render(request,'testbuttonpanel.html')
def competitions(request):
    return render(request,'competitions.html')
def contact(request):
    return render(request,'contact.html')
def soon(request):
    return render(request,'regsoon.html')
def safety(request):
    return render(request,'safety_in_aerospace.html')
def careers(request):
    return render(request,'careers_in_aerospace.html')
def liquid(request):
    return render(request,'liquid_engine_lecture.html')
def women(request):
    return render(request,'women.html')
def entrepreneurship(request):
    return render(request,'entrepreneurship.html')
def lectures(request):
    return render(request,'lectures.html')
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