from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Блогер')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
