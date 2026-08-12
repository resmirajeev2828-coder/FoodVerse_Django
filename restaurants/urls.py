from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path("api/", views.restaurant_api, name="restaurant_api"),
    path("api/<int:id>/", views.restaurant_detail_api, name="restaurant_detail_api"),
    path('<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    
]