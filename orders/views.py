import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from helpers.cart import getCartInfo
from items.models import Item, Category
from orders.forms import OrderConfirmForm
from orders.models import Order, OrderItem, ShippingAddress, Customer


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

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item, ordered=False)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    form = OrderConfirmForm(request.POST or None)
    items, order, cartItems = getCartInfo(request.user)
    categories = Category.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'form': form, 'categories': categories}

    if request.user.is_authenticated:
        customer = Customer.objects.get(user_id=request.user.id)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=cleaned_data['address'],
                city=cleaned_data['city'],
            )
            order.order_items.update(ordered=True)

            return redirect('promotions:home')

    return render(request, 'orders/checkout.html', context)
