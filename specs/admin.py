from django.contrib import admin

from .models import *

class CategoryFeatureAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'category', 'feature_name', 'feature_filter_name', 'unit', )
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'category')
    # какие поля будут участвовать в поиске
    search_fields = ('category', 'feature_name', 'feature_filter_name', 'unit',)



class ProductFeaturesAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'product', 'feature', 'value',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'product',)
    # какие поля будут участвовать в поиске
    search_fields = ('value',)



class FeatureValidatorAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'category', 'feature_key', 'valid_feature_value',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'category')
    # какие поля будут участвовать в поиске
    search_fields = ('category', 'feature_key', 'valid_feature_value',)



# Регистрируем модели в админке

admin.site.register(CategoryFeature, CategoryFeatureAdmin)
admin.site.register(ProductFeatures, ProductFeaturesAdmin)
admin.site.register(FeatureValidator, FeatureValidatorAdmin)

