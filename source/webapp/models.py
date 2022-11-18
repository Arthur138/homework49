from django.db import models

# Create your models here.
class Status(models.Model):
    statusname = models.CharField(max_length=150, null=False, blank=False, verbose_name="Статус")

    def __str__(self):
        return f'{self.pk}. {self.statusname}'

class Type(models.Model):
    typename = models.CharField(max_length=150, null=False, blank=False, verbose_name="Тип")

    def __str__(self):
        return f'{self.pk}. {self.typename}'

class Doings(models.Model):
    summary = models.CharField(max_length=200, null= False, blank= False, verbose_name="Краткое описание")
    description = models.TextField(max_length=2000, null= True, blank=True, verbose_name="Описание")
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name="Статус")
    type = models.ForeignKey('webapp.Type', related_name='type', on_delete=models.PROTECT, verbose_name="Тип")
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создание')
    update = models.DateTimeField(auto_now=True, verbose_name='Обновление')

    def __str__(self):
        return f'{self.pk}. {self.summary}'