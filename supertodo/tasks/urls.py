from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks_list, name='task-list'),
#     path('add/', views.post_add, name='post_add'),
#     path('<slug:post_slug>/', views.post_detail, name='post_detail'),
#     path('<slug:post_slug>/edit/', views.post_edit, name='post_edit'),
]