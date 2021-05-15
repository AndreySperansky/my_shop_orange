from django.contrib import admin

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'name', 'slug', )
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'name',)
    # какие поля будут участвовать в поиске
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'category', 'title', 'slug', 'price',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'category', 'title',)
    # какие поля будут участвовать в поиске
    search_fields = ('name', 'category', 'title',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
