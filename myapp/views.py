from django.shortcuts import render
from myapp.models import ModelName


def index(request):
    return render(request, 'index.html')

def viewname(request):
    data = ModelName.objects.all() 	//this is an example
    return render(request, 'some_template.html', {'data' : data} 	