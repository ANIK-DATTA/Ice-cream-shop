from django.shortcuts import redirect, render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = Contact(name = name, email=email, msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Message sent successfully.')

    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")

