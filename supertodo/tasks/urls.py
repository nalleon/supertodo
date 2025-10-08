from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('completed/', views.task_list_completed, name='task-list-completed'),
    path('pending/', views.task_list_pending, name='task-list-pending'),
    path('add/', views.add_task, name='task-add'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
    path('<slug:task_slug>/delete/', views.delete_task, name='task-delete'),
    path('<slug:task_slug>/edit/', views.edit_task, name='task-edit'),
    path('<slug:task_slug>/toggle/', views.toggle_task, name='task-toggle'),
]
