from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.utils.text import slugify


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/tasklist.html', {'tasks': tasks})

def task_list_pending(request):
    return


def task_list_completed(request):
    return


def task_detail(request, task_slug: str):
    return


def add_task(request):
    return


def delete_task(request, task_slug: str):
    return


def edit_task(request, task_slug: str):
    return


def toggle_task(request, task_slug: str):
    return
