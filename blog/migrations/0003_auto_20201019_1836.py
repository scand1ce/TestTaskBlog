# Generated by Django 3.1.2 on 2020-10-19 15:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201019_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['subscription_no']},
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('blog_id', 'user_id')},
        ),
    ]