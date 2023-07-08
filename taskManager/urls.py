from django.urls import path
from .view.sprint.views import SprintCreate, SprintDeleteView, SprintUpdate, DeleteView, SprintViewSet, SprintUpdate, SprintListView,  BoardList,BoardUpdate
from .view.task.views import TaskList,TaskDetail, TaskCreate, TaskUpdate, DeleteView
from .view.user.views import UserSignUpListView, UserLoginListView
from .view.project.views import ProjectCreate, ProjectDeleteView, ProjectUpdate, ProjectView, ProjectListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('board/', BoardList.as_view(), name='board'), 
    path('board/<int:pk>/', BoardUpdate.as_view(), name='board_view'), 


    path('task/', TaskList.as_view(), name='tasks'),
    path('register/', UserSignUpListView.as_view(), name='user_sign_up'),
    path('login/', UserLoginListView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),

    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate, name='task_form'),
    path('task-update/<int:pk>/', TaskUpdate, name='task_update'), 
    path('task-delete/<int:pk>/', DeleteView, name='task_delete'),

    path('sprint/', SprintListView.as_view(), name='sprint_list'), 
    path('sprint-create/', SprintCreate, name='sprint_form'), 
    path('sprint/<int:pk>/', SprintViewSet.as_view(), name='sprint'), 
    path('sprint-update/<int:pk>/', SprintUpdate, name='sprint_update'), 
    path('sprint-delete/<int:pk>/', SprintDeleteView, name='sprint_delete'),

    path('', ProjectListView.as_view(), name='project_list'), 
    path('project-create/', ProjectCreate, name='project_form'), 
    path('project/<int:pk>/', ProjectView, name='project'), 
    path('project-update/<int:pk>/', ProjectUpdate, name='project_update'), 
    path('project-delete/<int:pk>/', ProjectDeleteView, name='project_delete'),

]