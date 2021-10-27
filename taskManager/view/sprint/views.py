from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from taskManager.model.sprint.models import Sprint
from django.urls import reverse_lazy


class SprintViewSet(LoginRequiredMixin, DetailView):
    model = Sprint
    context_object_name = 'sprint'
    fields = '__all__'
    template_name = "sprint/sprint.html"
    success_url = reverse_lazy('sprint')


    search_fields = ('name',)
    ordering_fields = ('end', 'name',)

# class SprintDetail(LoginRequiredMixin, DetailView):
#     model = Sprint
#     context_object_name = 'sprint'
#     template_name = 'sprint/main.html'
class SprintListView(ListView):
    model = Sprint
    template_name = "sprint_list.html"

class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    context_object_name = 'sprint'
    success_url = reverse_lazy('tasks')
    template_name = "sprint/sprint_delete.html"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class SprintCreate(LoginRequiredMixin, CreateView):
    model = Sprint
    fields = '__all__'
    template_name = "sprint/sprint_form.html"
    success_url = reverse_lazy('sprint')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SprintCreate, self).form_valid(form)

class SprintUpdate(LoginRequiredMixin, UpdateView):
    model = Sprint
    fields = '__all__'
    template_name = "sprint/sprint_update.html"
    success_url = reverse_lazy('tasks')
