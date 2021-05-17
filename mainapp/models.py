from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:category_detail', kwargs={'slug': self.slug})


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(default=True)
    features = models.ManyToManyField("specs.ProductFeatures", blank=True, related_name='features_for_product')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', kwargs={'slug': self.slug})

    def get_features(self):
        return {f.feature.feature_name: ' '.join([f.value, f.feature.unit or ""]) for f in self.features.all()}
