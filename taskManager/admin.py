from django.contrib import admin

from taskManager.model.sprint.models import Sprint
from .model.task.models import Task
from .model.project.models import Project

admin.site.register(Task)
admin.site.register(Sprint)
admin.site.register(Project)

