from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class RegisterPage(FormView):
    template_name = 'taskManager/user_sign_up.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')



class CustomLoginView(LoginView):
    template_name = 'taskManager/user_login.html'
    fields = '__all__'
    # redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')