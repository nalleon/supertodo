from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.utils.text import slugify


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/tasklist.html', {'tasks': tasks})


def task_list_pending():
    return


def task_list_completed():
    return


def task_detail():
    return


def add_task():
    return


def delete_task():
    return


def edit_task():
    return


def toggle_task():
    return
