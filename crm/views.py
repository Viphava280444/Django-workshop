from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request, "crm/register.html")

# Create your views here.
def homepage(request):

    data = [{'id':'1','firstname':'viphava', 'GPA':4.0},
               {'id':'2','firstname':'tankup', 'GPA':2.0}
               ]
    
    context = {'datas' : data}

    return render(request, "crm/index.html", context)