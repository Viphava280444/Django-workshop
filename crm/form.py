from django.forms import ModelForm
from .models import Task

class TaskFrom(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['title',]



