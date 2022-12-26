

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Status(models.Model):
    statusname = models.CharField(max_length=150, null=False, blank=False, verbose_name="Статус")

    def __str__(self):
        return f'{self.statusname}'

class Type(models.Model):
    typename = models.CharField(max_length=150, null=False, blank=False, verbose_name="Тип")

    def __str__(self):
        return f'{self.typename}'

class Doings(models.Model):
    summary = models.CharField(max_length=200, null= False, blank= False, verbose_name="Краткое описание")
    description = models.TextField(max_length=2000, null= True, blank=True, verbose_name="Описание")
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ManyToManyField('webapp.Type', related_name='type', blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновление')
    task = models.ForeignKey('webapp.Projects', related_name="doings",on_delete=models.CASCADE, verbose_name="Задача")
    def __str__(self):
        return f'{self.pk}. {self.summary}'


class Projects(models.Model):
    start_date =models.DateField(null=False,blank=False, verbose_name="Начало")
    end_date =models.DateField(null= True, blank=True, verbose_name="Конец")
    name = models.CharField(max_length=30, null=False,blank=False, verbose_name="Название")
    description = models.TextField(max_length=400,null=False,blank=False, verbose_name="Описание")
    users = models.ManyToManyField(get_user_model(), related_name='projects')

    class Meta:
        permissions = [
            ('can_add_users', "может добавлять участников"),
            ('can_delete_users', "может удалять участников")
        ]
    def __str__(self):
        return f'{self.name}'

