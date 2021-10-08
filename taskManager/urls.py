from django.urls import path
from .views import TaskList, RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('register/', RegisterPage.as_view(), name='user_sign_up'),
    path('login/', CustomLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),

]