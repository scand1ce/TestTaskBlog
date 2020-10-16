from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),

]