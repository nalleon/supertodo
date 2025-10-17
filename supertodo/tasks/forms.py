from django import forms
from .models import Task

# Model form for creating a new task
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')

# Model form for editing a new task
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')