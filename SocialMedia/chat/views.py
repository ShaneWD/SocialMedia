from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def chat_home(request):
    return HttpResponse("<h1>Chat Home</h1>")