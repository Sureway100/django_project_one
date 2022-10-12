from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Hello world, this is your home')


def index(request):
    return render(request, 'home.html', 
                  {'header': 'Welcome',
                   'name': 'david'})