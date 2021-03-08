from orders.models import Order


def getCartInfo(user):
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.order_items.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    return (items, order, cartItems)


