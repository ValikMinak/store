from django.contrib import admin
from django.utils.safestring import mark_safe

from orders.models import Order, OrderItem, ShippingAddress, Customer


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered',)


class AdminOrderItem(admin.ModelAdmin):
    list_display = ('id', 'item', 'quantity',)


# class AdminShippingAddress(admin.ModelAdmin):
#     list_display = ('id', 'customer', 'address', 'city', 'state', 'zip_code', 'date_added')


class AdminOrderCustomer(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email')


admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)
# admin.site.register(ShippingAddress, AdminShippingAddress)
admin.site.register(Customer, AdminOrderCustomer)
