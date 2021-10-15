from django.urls import path
from .view.task.views import TaskList,TaskDetail, TaskCreate, TaskUpdate, DeleteView
from .view.user.views import UserSignUpListView, UserLoginListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('register/', UserSignUpListView.as_view(), name='user_sign_up'),
    path('login/', UserLoginListView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),

    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task_form'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),    
]