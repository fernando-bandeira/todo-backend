from django.contrib import admin
from django.db import models
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = 'title', 'description', 'status'
    pass


admin.site.register(Todo, TodoAdmin)
