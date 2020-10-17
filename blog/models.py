from django.db import models
from django.urls import reverse

from users.models import Users


class UserBlog(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Владелец блога')

    def __str__(self):
        return str(self.owner.verbose_name)

    def get_absolute_url(self):
        url = reverse('detail_blog', args=[self.author.username, self.pk])
        return url

    class Meta:
        verbose_name = 'Блог пользователя'
        verbose_name_plural = 'Блоги пользователей'


class NewsBlog(models.Model):
    user_blog = models.ForeignKey(UserBlog, on_delete=models.CASCADE, verbose_name='Блог', blank=False, null=False,
                                  related_name='news')
    author = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Автор', blank=False,
                               null=False)
    title = models.CharField(max_length=150, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    news_text = models.TextField(max_length=600, blank=True, verbose_name='Текст')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Новость блога'
        verbose_name_plural = 'Новости блога'
        ordering = ['-title', '-created_at']