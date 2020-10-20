from django.urls import path
from .views import BlogView, ListBlogView

urlpatterns = [
    path('blogs/', ListBlogView.as_view(), name='list_blog'),
    path('blog/<int:pk>/', BlogView.as_view(), name='detail_blog'),

]