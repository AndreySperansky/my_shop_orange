# mainapp/views

from random import random
from django.db.models import Q
from django.db import transaction
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, View
from .models import Category, Product
from basketapp.models import Basket
from specs.models import ProductFeatures
from .mixins import BasketMixin




class MyQ(Q):

    default = 'OR'

# **************************************************************************************

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(category__is_active=True)

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products

# ***********************************************************************************************

class MainView(BasketMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()[:6]
        basket = self.basket
        context = {
            'categories': categories,
            'products': products,
            'basket': basket,
            'title': 'Home'
        }
        return render(request, 'mainapp/index.html', context)


# ***********************************************************************************************

class CategoryDetailView(BasketMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'mainapp/products.html'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        category = self.get_object()
        context['basket'] = self.basket
        context['categories'] = self.model.objects.all()

        # сортировка по котегориям
        if not query and not self.request.GET:
            context['category_products'] = category.product_set.all()
            return context
        if query:
            products = category.product_set.filter(Q(title__icontains=query))
            context['category_products'] = products
            return context

        url_kwargs = {}
        for item in self.request.GET:
            if len(self.request.GET.getlist(item)) > 1:
                url_kwargs[item] = self.request.GET.getlist(item)
            else:
                url_kwargs[item] = self.request.GET.get(item)
        q_condition_queries = Q()

        for key, value in url_kwargs.items():
            if isinstance(value, list):
                q_condition_queries.add(Q(**{'value__in': value}), Q.OR)
            else:
                q_condition_queries.add(Q(**{'value': value}), Q.OR)
        pf = ProductFeatures.objects.filter(
            q_condition_queries
        ).prefetch_related('product', 'feature').values('product_id')
        products = Product.objects.filter(id__in=[pf_['product_id'] for pf_ in pf])
        context['category_products'] = products
        return context


class ProductDetailView(DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'mainapp/__product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_object().category.__class__.objects.all()
        # context['cart'] = self.cart
        return context


# *******************************************************************************************


def products(request, slug=None):
    basket = get_basket(request.user)
    title = 'продукты'
    links_menu = Category.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'basket': basket,
    }


    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category__slug=slug, is_active=True).order_by('price')

# ***************************** pagination ********************************************

    # paginator = Paginator(products, 2)
    # try:
    #     products_paginator = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paginator = paginator.page(1)
    # except EmptyPage:
    #     products_paginator = paginator.page(paginator.num_pages)
# ***************************** pagination ********************************************

    content['category'] = category
    content['products'] = products
    # content['products'] = products_paginator

    # return render(request, 'mainapp/products.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content['same_products'] = same_products
    content['hot_product'] = hot_product
    return render(request, 'mainapp/products.html', content)
