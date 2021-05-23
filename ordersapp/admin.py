from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user',  'status', 'created', 'updated', 'is_active',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id',  'user',  'status',)
    # какие поля будут участвовать в поиске
    search_fields = ('user',  'status', 'is_active')


class OrderItemAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'order', 'product', 'quantity',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'order', 'product', 'quantity',)
    # какие поля будут участвовать в поиске
    search_fields = ('product',)



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
