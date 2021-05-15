from django.contrib import auth
from django.views.generic import View
from basketapp.models import Basket


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