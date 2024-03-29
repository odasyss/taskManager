from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView
#from taskManager.model.task.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
#from taskManager.model.task.models import Task


from taskManager.models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task/task_list.html"


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/main.html'


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    login_url = '/login/'
    success_url = reverse_lazy('tasks')
    template_name = "taskManager/task_delete.html"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    login_url = '/login/'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    login_url = '/login/'
    template_name = "taskManager/task_update.html"
    success_url = reverse_lazy('tasks')
