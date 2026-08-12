from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path("order-success/", views.order_success, name="order_success"),

    path("orders/", views.order_history_api, name="order_history"),
    path("remove/<int:id>/", views.remove_from_cart, name="remove_from_cart"),

    path("api/cart/", views.get_cart, name="get_cart"),
    path("api/create/", views.create_order, name="create_order"),
    path("api/history/", views.order_history_api, name="order_history_api"),

    path("increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
]