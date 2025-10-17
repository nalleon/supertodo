from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import AddTaskForm
from .forms import EditTaskForm

from django.utils.text import slugify
import datetime


def task_list(request):
    tasks = Task.objects.all().order_by('-updated_at')
    return render(request, 'tasks/tasklist.html', {'tasks': tasks, 'subtitle': 'Todas las tareas'})


def task_list_pending(request):
    pending_tasks = Task.objects.filter(completed=False).order_by('-updated_at')

    return render(
        request, 'tasks/tasklist.html', {'tasks': pending_tasks, 'subtitle': 'Tareas pendientes'}
    )


def task_list_completed(request):
    completed_tasks = Task.objects.filter(completed=True).order_by('-updated_at')

    return render(
        request, 'tasks/tasklist.html', {'tasks': completed_tasks, 'subtitle': 'Tareas completadas'}
    )


def task_detail(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)
    except Task.DoesNotExist:
        return render(request, 'tasks/task/tasknotexists.html', {'task_slug': task_slug})

    return render(
        request, 'tasks/task/taskdetails.html', {'task': task, 'subtitle': 'Task Details'}
    )


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.completed = False
            task.created_at = datetime.datetime.now()
            task.updated_at = datetime.datetime.now()
            task.save()

            return redirect('tasks:task-list')

    else:
        form = AddTaskForm()

    return render(request, 'tasks/task/taskadd.html', dict(form=form, subtitle='Añadir tarea'))


def delete_task(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)

    except Task.DoesNotExist:
        return render(request, 'tasks/task/tasknotexists.html', {'task_slug': task_slug})
    task.delete()
    return redirect('tasks:task-list')


def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)

    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.updated_at = datetime.datetime.now()
            task.save()
            return redirect('tasks:task-detail', task.slug)

    else:
        form = EditTaskForm(instance=task)

    return render(
        request, 'tasks/task/taskedit.html', dict(task=task, form=form, subtitle='Editar tarea')
    )


def toggle_task(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)

    except Task.DoesNotExist:
            return render(request, 'tasks/task/tasknotexists.html', {'task_slug': task_slug})
    task.completed = not task.completed
    task.updated_at = datetime.datetime.now()
    task.save()

    return redirect('tasks:task-list')
