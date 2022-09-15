from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    # retrieves all tasks from the database
    tasks = Task.objects.all()


    if request.method =="POST":
        data = request.POST
        task = data.get("task")
        tasks.append(task)
        # add task into the database
        Task.objects.create(title=task)

    context = {
        "tasks": tasks
        }
    return render(request, "base.html", context)