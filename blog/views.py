from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from blog.forms import CreateNewsForm, CreateSubForm
from blog.models import Blog



class ListBlogView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogView(FormMixin, DetailView):
    model = Blog
    template_name = 'blog/detail_blog.html'
    form_class = CreateNewsForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_blog', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_blog = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class SubscribeView(FormMixin, ListView):
    form_class = CreateSubForm
    model = Blog
    success_url = reverse_lazy('list_blog')
    template_name = 'blog/detail_blog.html'

    def form_valid(self, form):
        return super().form_valid(form)
