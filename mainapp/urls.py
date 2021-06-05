from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('brand/<int:pk>/', BrandView.as_view(), name='brand_detail'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('bookmarks/add/<int:pk>/', add_remove_bookmark, name='bookmark_add'),
    path('bookmarks/remove/<int:pk>/', bookmark_remove, name='bookmark_remove'),
    path('bookmarks/', bookmarks, name='bookmarks'),
    path('bookmarks/list/', bookmark_list, name='bookmark_list'),
]