from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

__all__ = (
    'CategoryItems',
    'SingleItem',
    'CategoryChildren',
)

from items.models import Category, Item
from orders.models import Order


class CategoryItems(LoginRequiredMixin, ListView):
    template_name = 'items/category_items.html'
    context_object_name = 'items'
    paginate_by = 3

    def get_queryset(self):
        return Item.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(customer=self.request.user.customer)
        context['title'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['cartItems'] = order.get_cart_items
        return context


class SingleItem(DetailView):
    model = Item
    template_name = 'items/single_item.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(customer=self.request.user.customer)
        context['title'] = get_object_or_404(Item, pk=self.kwargs['pk'])
        context['categories'] = Category.objects.all()
        context['cartItems'] = order.get_cart_items
        return context


class CategoryChildren(ListView):
    model = Category
    template_name = 'items/category_children.html'
    context_object_name = 'category_children'

    def get_queryset(self):
        return Category.objects.get(slug=self.kwargs['slug']).children.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(customer=self.request.user.customer)
        context['title'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['cartItems'] = order.get_cart_items
        return context
