from django.db import models
from django.contrib.auth.models import User

from items.models import Item


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупателя"
        verbose_name_plural = "Покупатели"
        ordering = ['-pk']


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"
        ordering = ['-date_ordered']

    # @property
    # def shipping(self):
    #     shipping = False
    #     orderitems = self.orderitem_set.all()
    #     for i in orderitems:
    #         if i.product.digital == False:
    #             shipping = True
    #     return self.shipping
    #
    @property
    def get_cart_total(self):
        orderitems = self.order_items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_items.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Заказанные товары"
        ordering = ['-date_added']

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-date_added']
