# Generated by Django 3.1.2 on 2020-10-19 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Блог пользователя',
                'verbose_name_plural': 'Блоги пользователей',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('news_text', models.TextField(blank=True, max_length=600, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Новость блога',
                'verbose_name_plural': 'Новости блога',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_no', models.AutoField(primary_key=True, serialize=False)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
