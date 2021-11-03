from taskManager.model.project.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import query
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from taskManager.model.sprint.models import Sprint
from django.urls import reverse_lazy
from taskManager.model.task.models import Task


class ProjectView(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'
    fields = '__all__'
    template_name = "project/project.html"
    success_url = reverse_lazy('project_list')
    search_fields = ('name')
    ordering_fields = ('end', 'name',)



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project'
    template_name = "project/project_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['Sprint'] = Sprint.objects.all()
        context['tasks'] = Task.objects.all()
        return context

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_list')
    template_name = "project/project_delete.html"

    #def get_queryset(self):
    #    owner = self.request.user
    #    return self.model.objects.filter(user=owner)

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')
    template_name = "taskManager/project_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    template_name = "project/project_update.html"
    success_url = reverse_lazy('project_list')
