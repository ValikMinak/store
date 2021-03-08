from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('promotion/<str:slug>', home, name='home')
]
