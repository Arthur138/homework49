# Generated by Django 4.1.2 on 2022-12-22 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_remove_projects_task_doings_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]