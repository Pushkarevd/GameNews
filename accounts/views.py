from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

from accounts.form import CreateUserForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Профиль' + user + 'был создан!')
            return redirect('/accounts/login')
    return render(request, 'signup.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Имя пользователя или пароль не верны!")
    return render(request, 'registration/login.html')
