from django.urls import path
from .views import HomePageView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('password/', auth_views.PasswordChangeView.as_view(template_name = 'users/password_change_form.html')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('home/', HomePageView.as_view(), name='home'),
]