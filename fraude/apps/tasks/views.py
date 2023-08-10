from django.shortcuts import render
from django.http import HttpResponse
from apps.tasks import *
# Create your views here.

#home
def inicio(request):
    return render(request,'paginas/inicio.html')

#create
def create(request):
    return render(request,'paginas/create.html')

#view
def view(request):
    return render(request,'paginas/view.html')

#edit
def edit(request):
    return render(request,'paginas/edit.html')