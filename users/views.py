from django.views.generic import TemplateView, ListView
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/users_list.html'

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        return False