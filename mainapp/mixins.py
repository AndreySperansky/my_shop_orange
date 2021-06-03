from django.contrib import auth
from random import random
from django.views.generic import View
from basketapp.models import Basket
from mainapp.models import Product


class BasketMixin(View):

    model = Basket

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            basket = Basket.objects.filter(user=user)
        else:
            basket = []

        self.basket = basket
        return super().dispatch(request, *args, **kwargs)


class CategoryMixin(View):

    def dispatch(self, request, *args, **kwargs):
        current_page = request.resolver_match.kwargs['slug']

        self.current_page = current_page
        return super().dispatch(request, *args, **kwargs)



class ProductMixin(View):
    model = Product

    # def get_hot_product(self):
    #     self.products = Product.objects.filter(category__is_active=True)

    #     return random.sample(list(self.products), 1)[0]

    # def get_same_products(self, hot_product):
    #     self.same_products = Product.objects.filter(category=hot_product.category). \
    #                         exclude(pk=hot_product.pk)[:3]
    #     return self.same_products

    def dispatch(self, request, slug=None, *args, **kwargs):

        self.products = Product.objects.filter(category__slug=slug, is_active=True).order_by('price')

        return super().dispatch(request, slug, *args, **kwargs)