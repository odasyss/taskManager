from taskManager.model.project.models import Project


class ProjectView():
    model = Project
    search_fields = ('name')