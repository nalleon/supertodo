from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=256, blank=True)
    slug = models.SlugField(unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'PK: {self.pk} | name: {self.name} | description: {self.description} | slug: {self.slug} | completed: {self.completed} | created_at: {self.created_at} | updated_at: {self.updated_at}'
