from django.views.decorators.http import require_safe, require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .get_methods import get_form_values, get_username_and_password


@require_safe
def register_page(request):
    return render(request, "accounts/register.html")


@require_POST
def register(request):
    form_values = get_form_values(request)

    if form_values.password == form_values.password2:
        if User.objects.filter(username=form_values.username).exists():
            messages.error(request, "This username already exists.")
            return redirect("accounts:register_page")
        else:
            if User.objects.filter(email=form_values.email).exists():
                messages.error(request, "That email is being used")
                return redirect("accounts:register_page")
            else:
                user = User.objects.create_user(
                    username=form_values.username,
                    password=form_values.password,
                    email=form_values.email,
                    first_name=form_values.first_name,
                    last_name=form_values.last_name,
                )
                user.save()
                messages.success(request, "You are now registered and can log in")
                return redirect("accounts:login_page")
    else:
        messages.error(request, "Passwords do not match")
        return redirect("accounts:register_page")


@require_safe
def login_page(request):
    return render(request, "accounts/login.html")


@require_POST
def login(request):
    user_credentials = get_username_and_password(request)

    user = auth.authenticate(
        username=user_credentials.username, password=user_credentials.password
    )

    if user is not None:
        auth.login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("accounts:dashboard")
    else:
        messages.error(request, "Invalid credentials")
        return redirect("accounts:login_page")


@require_POST
def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out")
    return redirect("pages:index")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
