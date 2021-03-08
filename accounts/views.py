from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, UserRegistrationForm
from items.models import Category
from orders.models import Customer


def login_view(request):
    categories = Category.objects.all()
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get(
        'next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'accounts/login.html', {'form': form, 'categories': categories})


def logout_view(request):
    logout(request)
    return redirect('/')


def registration_view(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password_confirm'])
            new_user.save()
            Customer(user=new_user, name=new_user.username, email=new_user.email).save()

            return render(request, 'accounts/register_done.html', {'new_user': new_user})
        return render(request, 'accounts/register.html', {'form': form,'categories':categories})


    else:
        categories = Category.objects.all()
        form = UserRegistrationForm(request.POST)
        return render(request, 'accounts/register.html', {'form': form,'categories':categories})
