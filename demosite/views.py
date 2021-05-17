from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    values = {'name':'ABHISHEK', 'age':23, 'city':'pune'}
    return render(request, 'home.html', values)