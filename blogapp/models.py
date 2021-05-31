from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    # Чтобы представить строковое представление поля модели используем метод __str__
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('view_posts', kwargs={"pk": self.pk})        # ????


    # Изменение отображения заголовка модели в админке
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

