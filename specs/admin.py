from django.contrib import admin

from .models import *

# Регистрируем модели в админке

admin.site.register(ProductFeatures)
admin.site.register(FeatureValidator)
admin.site.register(CategoryFeature)
