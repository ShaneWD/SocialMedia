from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {

    }
    return render(request, "main/home.html", context)