from django.urls import path
from .views import BlogView, ListBlogView



urlpatterns = [
    path('blogs/', ListBlogView.as_view(template_name='blog/blog_list.html'), name='list_blog'),
    path('blog/<int:pk>/', BlogView.as_view(template_name='blog/blog.html'), name='detail_blog'),

]