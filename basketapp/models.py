from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="fk_product")
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    # basket = request.user.basket.all - получение объектов корзины текущего пользователя в контроллерах

    def __str__(self):
        return f'{self.user}: {self.product.title}, {self.product.quantity}'


    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        "return total cost for user"
        _items = Basket.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    # @staticmethod
    # def get_items(user):
    #     return Basket.objects.all()

    @staticmethod
    def get_items(user):
        '''Получение всех корзин пользователя'''
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_item(pk):
        '''Получение одной конкретной корзины  пользователя'''
        return Basket.objects.filter(pk=pk).first()

    @classmethod
    def get_products_quantaty(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic


    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
    #         # self.__class__.get_item  - обращение к статическому классу
    #     else:
    #         # если pk не передан
    #         self.product.quantity -= self.quantity
    #     self.product.save()  # сохраняем остатки, связанные с данной корзиной
    #     super(self.__class__, self).save(*args, **kwargs)  # сохраняем остатки у родителя
    #
    #
    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(self.__class__, self).delete()
