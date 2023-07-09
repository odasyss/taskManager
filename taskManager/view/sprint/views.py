from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import query
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from taskManager.model.sprint.models import Sprint
from django.urls import reverse_lazy
#from .model.task.models import Task
from taskManager.models import Sprint, Task, Project
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import Group
from django import forms
register = template.Library()

class SprintViewSet(DetailView):
    model = Sprint
    context_object_name = 'sprint'
    fields = '__all__'
    template_name = "sprint/sprint.html"
    success_url = reverse_lazy('tasks')


    search_fields = ('name',)
    ordering_fields = ('end', 'name',)

class SprintListView(ListView):
    model = Sprint
    context_object_name = 'sprint'
    template_name = "sprint/sprint_list.html"

    def get_context_data(self, **kwargs):
        context = super(SprintListView, self).get_context_data(**kwargs)   
        context['projects'] = Project.objects.all()
        context['sprints'] = Sprint.objects.all()
        context['tasks'] = Task.objects.all()
        return context
    #@register.filter
    #def in_task(Task, name):
    #    return Task.filter(name=name)

    #def get_context_data(self, **kwargs):
    #    context = super(SprintListView, self).get_context_data(**kwargs)
        # context['Sprint'] = Sprint.objects.get()
    #    context['tasks'] = Task.objects.all()
    #    return context
# queryset = Task.objects.all().filter(sprint=self.request.id)

    #def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['sprint_list'] = Task.objects.all()
        #return context

class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    context_object_name = 'sprint'
    login_url = '/login/'
    success_url = reverse_lazy('tasks')
    template_name = "sprint/sprint_delete.html"

    #def get_queryset(self):
    #    owner = self.request.user
    #    return self.model.objects.filter(user=owner)

class SprintCreate(LoginRequiredMixin, CreateView):
    model = Sprint
    fields = '__all__'
    login_url = '/login/'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SprintCreate, self).form_valid(form)
    widgets = {
        'launch_date': forms.DateInput(
            format=('%Y-%m-%d'),          # <== This line solves the issue
            attrs={'class': 'form-control',
                   'type': 'date'
            }),
    }


class SprintUpdate(LoginRequiredMixin, UpdateView):
    model = Sprint
    fields = '__all__'
    login_url = '/login/'
    template_name = "sprint/sprint_update.html"
    success_url = reverse_lazy('tasks')

class BoardList(ListView):
    model = Sprint
    context_object_name = 'board'
    template_name = "taskManager/board.html"

    def get_context_data(self, **kwargs):
        context = super(BoardList, self).get_context_data(**kwargs)   
        context['projects'] = Project.objects.all()
        context['sprints'] = Sprint.objects.all()
        context['tasks'] = Task.objects.all()
        return context


class BoardUpdate(UpdateView):
    model = Sprint
    fields = '__all__'
    context_object_name = 'board'
    template_name = "taskManager/board_view.html"
    success_url = reverse_lazy('board')
