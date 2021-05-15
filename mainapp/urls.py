from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
]