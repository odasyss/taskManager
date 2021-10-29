from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from taskManager.model.sprint.models import Sprint
from django.urls import reverse_lazy


class SprintViewSet(LoginRequiredMixin, DetailView):
    model = Sprint
    context_object_name = 'sprint'
    template_name = "sprint/sprint.html"
    success_url = reverse_lazy('sprint_list')
    ordering_fields = ('end', 'name',)
class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    context_object_name = 'sprint'
    template_name = "sprint_list.html"
class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    context_object_name = 'sprint'
    template_name = "sprint/sprint_delete.html"
    success_url = reverse_lazy('sprint_list')

    # def get_queryset(self):
    #     owner = self.request.user
    #     return self.model.objects.filter(user=owner)

class SprintCreate(LoginRequiredMixin, CreateView):
    model = Sprint
    fields = '__all__'
    success_url = reverse_lazy('sprint_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SprintCreate, self).form_valid(form)


class SprintUpdate(LoginRequiredMixin, UpdateView):
    model = Sprint
    fields = '__all__'
    template_name = "sprint/sprint_update.html"
    success_url = reverse_lazy('sprint_list')
