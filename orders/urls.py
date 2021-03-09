from django.urls import path
from .views import *

urlpatterns = [
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    # path('checkout/process_order/', processOrder, name='process_order'),

]
