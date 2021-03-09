from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class OrderConfirmForm(forms.Form):
    city = forms.CharField(label='город',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': "Введите город",

                           }))
    address = forms.CharField(label='адрес',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': "Введите адрес",

                              }))
