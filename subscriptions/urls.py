from django.urls import path
from .views import SubscribersView

urlpatterns = [
    path('subscriptions/', SubscribersView.as_view(template_name='subscriptions/sub_list.html'), name='sub_list'),
]
