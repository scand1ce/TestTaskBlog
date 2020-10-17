from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Блогер'
        verbose_name_plural = 'Блогеры'
