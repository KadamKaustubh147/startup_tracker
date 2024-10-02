from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello, World. You are at chai aur Django Home page")
    return render(request, 'homepage.html')
