from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='имя',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': "Введите имя",

                               }))
    password = forms.CharField(label='пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': "Введите пароль",

                               }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Не верный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Пользователь неактивен')
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='имя',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': "Введите имя",

                               }))
    email = forms.EmailField(label='email',
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': "Введите email",

                             }))
    password = forms.CharField(label='пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': "Введите пароль",

                               }))
    password_confirm = forms.CharField(label='пароль-2',
                                       widget=forms.PasswordInput(attrs={
                                           'class': 'form-control',
                                           'placeholder': "Повторите пароль",

                                       }))

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password_confirm(self):
        data = self.cleaned_data
        if data['password'] != data['password_confirm']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password_confirm']
