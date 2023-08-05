from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#home
def inicio(request):
    return HttpResponse("<h1>Binevendio</h1>")

#create
def create(request):
    return HttpResponse("<h1>Create</h1>")

#home
def view(request):
    return HttpResponse("<h1>view</h1>")

#home
def edit(request):
    return HttpResponse("<h1>edit</h1>")