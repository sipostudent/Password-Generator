from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'kdfgbkebfh34873iy57thugkenb'})

def password(request):
    return render(request, 'generator/password.html')