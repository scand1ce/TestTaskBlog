from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.models import Blog
from subscriptions.models import Subscriptions


class SubscribersView(CreateView):
    model = Subscriptions
    fields = ['blog', 'user']
    success_url = reverse_lazy('subscriptions:subscriptions')
    template_name = 'subscriptions/sub_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs.get('pk'))
        return super(SubscribersView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SubscribersView, self).get_form_kwargs()
        if self.request.method == 'POST':
            data = dict(kwargs['data'])
            data.update({
                'blog': self.blog.pk,
                'user': self.request.user.pk,
            })
            kwargs['data'] = data
        return kwargs