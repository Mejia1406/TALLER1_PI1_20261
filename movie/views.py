from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name': 'Samuel Moncada'})

def about(request):
    return HttpResponse("<h1>About Movie Reviews</h1>")