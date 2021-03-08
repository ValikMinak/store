import json

from django.http import JsonResponse
from django.shortcuts import render

from helpers.cart import getCartInfo
from items.models import Item, Category
from orders.models import Order, OrderItem


def cart(request):
    items, order, cartItems = getCartInfo(request.user)

    categories = Category.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'categories': categories}
    return render(request, 'orders/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']

    customer = request.user.customer
    item = Item.objects.get(pk=itemId)
    order, created = Order.objects.get_or_create(customer=customer)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
