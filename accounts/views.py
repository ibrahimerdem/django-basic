from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(req):
    context = {}
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid name or pass'}
            return render(req, 'accounts/login_form.html', context=context)
        login(req, user)
        return redirect('/')
    return render(req, 'accounts/login_form.html', context=context)


def logout_view(req):
    context = {}
    return render(req, 'accounts/logout_form.html', context=context)


def register_view(req):
    context = {}
    return render(req, 'accounts/register_form.html', context=context)
