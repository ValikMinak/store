from django.shortcuts import render

from helpers.cart import getCartInfo
from items.models import Item, Category
from promotions.models import Promotion


def home(request):
    items, order, cartItems = getCartInfo(request.user)

    promotions = Promotion.objects.all()
    categories = Category.objects.all()

    context = {'promotions': promotions, 'categories': categories, 'items': items, 'order': order,
               'cartItems': cartItems, 'categories': categories}
    return render(request, 'promotions/home.html', context)
