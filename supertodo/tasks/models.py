from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=256, blank=True)
    slug = models.SlugField(unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # def __str__ (self):
    #     return f'PK:'

