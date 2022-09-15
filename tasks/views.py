from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    tasks = [
        "fill petrol in the car",
        "modify the car",
        "clean the car",
        "test the car"
    ]

    context = {
        "tasks": tasks
        }
    return render(request, "base.html", context)