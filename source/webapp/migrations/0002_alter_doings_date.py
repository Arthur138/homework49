# Generated by Django 4.1.2 on 2022-11-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doings',
            name='date',
            field=models.TextField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
