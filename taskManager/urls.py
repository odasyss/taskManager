from django.urls import path
from .view.task.views import TaskList, TaskCreate
from .view.user.views import UserSignUpListView, UserLoginListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('register/', UserSignUpListView.as_view(), name='user_sign_up'),
    path('login/', UserLoginListView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
    path('create/', TaskCreate.as_view(), name='task_create'),
]