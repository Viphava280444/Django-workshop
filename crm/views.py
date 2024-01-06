from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def register(request):
    return render(request, "crm/register.html")

def task(request):
    queryDataAll = Task.objects.all()
    context = {'allTasks': queryDataAll}
    return render(request, "crm/task.html", context)

# Create your views here.
def homepage(request):

    data = [{'id':'1','firstname':'viphava', 'GPA':4.0},
               {'id':'2','firstname':'tankup', 'GPA':2.0}
               ]
    
    context = {'datas' : data}

    return render(request, "crm/index.html", context)