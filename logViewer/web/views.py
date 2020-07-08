from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate


def index(request):
    template = loader.get_template('web/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('registration/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def validate(request):    
    user = authenticate(username='john', password='secret')
    if user is not None:
        return
        # A backend authenticated the credentials
    else:
        return
        # No backend authenticated the credentials