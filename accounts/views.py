from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def login_view(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('/')
    else:
        form = AuthenticationForm(req)
    context = {'form': form}
    return render(req, 'accounts/login_form.html', context=context)


def logout_view(req):
    if req.method == 'POST':
        logout(req)
        return redirect('/')
    context = {}
    return render(req, 'accounts/logout.html', context=context)


def register_view(req):
    form = UserCreationForm(req.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login/')
    context = {'form': form}
    return render(req, 'accounts/register_form.html', context=context)
