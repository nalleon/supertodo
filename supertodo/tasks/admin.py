from django.contrib import admin


from .models import Task

@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'slug', 'completed', 'created_at', 'updated_at')