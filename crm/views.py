from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse('This is a registeration page.')

# Create your views here.
def homepage(request):
    return HttpResponse('This is the homepage.')