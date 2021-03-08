from django.urls import path
from .views import *

urlpatterns = [
    path('', updateItem, name='update_item'),
]
