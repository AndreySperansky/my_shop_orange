from django.urls import path
from .views import main, ViewPost

app_name = 'blogapp'

urlpatterns = [
    path('', main, name='main'),
    path('posts/<int:pk>/', ViewPost.as_view(), name = 'post')
]