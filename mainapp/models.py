from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
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
    # description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    features = models.ManyToManyField("specs.ProductFeatures", blank=True, related_name='features_for_product')
    bookmarks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='BookmarkProduct',
        related_name='bookmark_creator',
        verbose_name='владелец закладки',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', kwargs={'slug': self.slug})

    def get_features(self):
        return {f.feature.feature_name: ' '.join([f.value, f.feature.unit or ""]) for f in self.features.all()}


# Промежуточная таблица

class BookmarkProduct(models.Model):
    shop_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookmark_holder',
        verbose_name='Полкупатель')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='bookmarked_product',
        verbose_name='Товар')

    def __str__(self):
        return f'{self.product.title}, {self.product.price}'

    class Meta:
        verbose_name = 'Избранные товары'
        verbose_name_plural = 'Избранные товары'
        ordering = ['product']