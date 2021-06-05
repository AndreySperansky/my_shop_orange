from django.shortcuts import render
from django.http import HttpResponse

from mainapp.mixins import BasketMixin
from .models import Posts
from basketapp.models import Basket
from mainapp.models import Category, Brand

from django.views.generic import ListView, DetailView, CreateView

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def main(request):
    posts = Posts.objects.all()
    basket = get_basket(request.user)
    # news = Posts.objects.order_by('-created_at')

    context = {
        'posts': posts,
        'basket': basket,
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'title': 'Blog',
    }
    # ключи из словарей затем используются в качестве переменных в шаблонах
    return render(request, 'blogapp/blog.html', context)
    # return render(request, template_name='news/index.html', context=context)


class ViewPost(BasketMixin, DetailView):
    model = Posts
    template_name = 'blogapp/post.html'
    context_object_name = 'item'    # по умолчанию - object
    # pk_url_kwarg = 'id_post'      # если в urls path параметр отличный от pk или id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = self.basket
        context['brands'] = Brand.objects.all()
        context['categories'] = Category.objects.all()

        return context


