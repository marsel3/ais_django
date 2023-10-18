from django.db import models


class Achievement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    date = models.DateTimeField(verbose_name='Дата и время', auto_now=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
