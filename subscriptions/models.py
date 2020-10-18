from django.db import models
from blog.models import Blog, New
from users.models import User


class Subscriptions(models.Model):
    user_sub = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик')
    subscriptions = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Подписки", blank=True)
    readed = models.ForeignKey(New, on_delete=models.CASCADE, related_name='Прочитано', blank=True)

    def __str__(self):
        return "Подписки блогера {}".format(self.user_sub)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
