from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todo:task_list")
    else:
        form = UserCreationForm()
    
    return render(request, "todo/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todo:task_list")
    return render(request, "todo/login.html")

def logout_view(request):
    logout(request)
    return redirect("todo:login")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todo:task_list")
    else:
        form = UserCreationForm()

    return render(request, "todo/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todo:task_list")
    return render(request, "todo/login.html")


def logout_view(request):
    logout(request)
    return redirect("todo:login")


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "todo/task_list.html", {"tasks": tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(user=request.user, title=title)
        return redirect("todo:task_list")

    return render(request, "todo/add_task.html")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.user == request.user:
        task.delete()
    return redirect("todo:task_list")

