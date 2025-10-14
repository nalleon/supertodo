from django import forms
from .models import Task

# Hay que ivestigar como darle estilo al ModelForm
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'completed', 'description')