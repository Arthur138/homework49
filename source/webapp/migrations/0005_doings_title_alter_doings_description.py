# Generated by Django 4.1.2 on 2022-11-06 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_doings_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doings',
            name='title',
            field=models.TextField(default=django.utils.timezone.now, max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doings',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Описание'),
        ),
    ]