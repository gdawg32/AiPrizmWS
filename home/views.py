from turtle import setundobuffer
from unicodedata import name
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Contact, Service, Team


# Create your views here.
def index(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def services(request):
    services = Service.objects.all()
    context = {
        "services": services
    }
    return render(request, 'home/services.html', context)   

def portfolio(request):
    return render(request, 'home/portfolio.html')

def portfolio_details(request):
    return render(request, 'home/portfolio-details.html')             

def team(request):
    team = Team.objects.all
    context = {
        "team":team,
    }
    return render(request, 'home/team.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        #send mail

        # send_mail(
        #    subject, #subject
        #    message, #message
        #    email, #sender mail
        #    ['gnroll98@gmail.com'] #to mail
        # )


        return render(request, 'home/contact.html') 
    else:    
        return render(request, 'home/contact.html')        