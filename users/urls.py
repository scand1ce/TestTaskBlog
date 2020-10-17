from django.urls import path
from .views import HomePageView, UsersListView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('users/', UsersListView.as_view(template_name='users/users_list.html'), name='users_list'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
]