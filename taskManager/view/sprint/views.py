from taskManager.model.sprint.models import Sprint


class SprintViewSet():
    model = Sprint
    search_fields = ('name',)
    ordering_fields = ('end', 'name',)