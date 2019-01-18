from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse("Placeholder to display blog " + num)

def edit(request, num):
    return HttpResponse("Placeholder to edit blog " + num)

def destroy(request, num):
    return redirect('/')


# Create your views here.
