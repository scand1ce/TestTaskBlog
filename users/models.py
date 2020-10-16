from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Блогер')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Эл. почта'),

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
