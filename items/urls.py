from django.urls import path
from .views import *

urlpatterns = [
    path('category/<str:slug>', CategoryItems.as_view(), name='category_items'),
    path('item/<int:pk>', SingleItem.as_view(), name='single_item')
]
