from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Salman Noor"

    context = {
        "name":name
    }
    return render(request, "base.html", context)