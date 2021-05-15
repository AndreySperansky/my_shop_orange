from django.urls import path
from .views import basket, checkout, basket_add, basket_remove


app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='cart'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('checkout/', checkout, name='checkout'),
]

