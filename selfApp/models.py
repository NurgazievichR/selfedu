from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    url = models.SlugField(null=True, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True,verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Фото', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания', blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время изменения', blank=True, null=True)
    is_published = models.BooleanField(default=True,verbose_name='опубликовано')

    #new
    url = models.SlugField(null=True, unique=True,verbose_name='Ссылка')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, default=None, blank=True,verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известность'
        verbose_name_plural = 'Известные люди'