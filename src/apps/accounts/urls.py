from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login", views.login, name="login"),
    path("login_page", views.login_page, name="login_page"),
    path("register", views.register, name="register"),
    path("register_page", views.register_page, name="register_page"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
