from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def chat_home(request):
    context = {

    }
    return render(request, "chat/chat_home.html", context)