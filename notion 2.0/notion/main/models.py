from django.db import models

# Create your models here.

class Notion(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'