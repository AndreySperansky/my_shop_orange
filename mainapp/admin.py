from django.contrib import admin

from .models import Category, Product, Brand, BookmarkProduct

class CategoryAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'name', 'slug',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'name', 'slug',)
    # какие поля будут участвовать в поиске
    search_fields = ('name',)


class BrandAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'name',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'name',)
    # какие поля будут участвовать в поиске
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    # Внесение добавления в админку
    change_form_template = 'custom_admin/change_form.html'
    # какие поля будут отображаться в админке
    list_display = ('id', 'category', 'brand', 'title', 'slug', 'price', 'quantity', 'is_new', 'is_sale', 'is_active')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'category', 'title',)
    # какие поля будут участвовать в поиске
    search_fields = ('name', 'category', 'title',)


class BookmarkProductAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'product', 'shop_user')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'product', 'shop_user',)
    # какие поля будут участвовать в поиске
    search_fields = ('product', 'shop_user',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BookmarkProduct, BookmarkProductAdmin)
