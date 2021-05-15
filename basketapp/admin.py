from django.contrib import admin

from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'product', 'quantity', 'add_datetime',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'user', 'product',)
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'product',)


admin.site.register(Basket, BasketAdmin)
