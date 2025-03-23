from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def new(request):
    context = {}
    template = loader.get_template('taches/new.html')
    return HttpResponse(template.render(context, request))