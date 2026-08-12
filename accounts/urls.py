from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("login_api/", views.login_api, name="login_api"),
    path("register_api/", views.register_api, name="register_api"),
]