from django.contrib import admin
from .models import Task
from .models import Project
from .models import Action
from .models import Sprint

admin.site.register(Sprint)
admin.site.register(Project)
admin.site.register(Action)
admin.site.register(Task)