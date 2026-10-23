from django.shortcuts import render 
from django.http import HttpResponse

def indexpageview(request):
    return render(request, 'index.html')

def adduserpageview(request):
    return render(request, 'adduser.html')