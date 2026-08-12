from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('api/', views.menu_api, name="menu_api"),
]