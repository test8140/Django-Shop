from django.urls import path
from ecomapp.views import base_view, category_view, product_view, add_to_cart_view, cart_view, remowe_from_cart_view

urlpatterns = [
    path('', base_view, name='base'),
    path('category/<str:slug>', category_view, name='category_detail'),
    path('product/<str:slug>', product_view, name='product_detail'),
    path('add_to_cart/<str:slug>', add_to_cart_view, name='add_to_cart'),
    path('remowe_from_cart/<str:slug>', remowe_from_cart_view, name='remowe_from_cart'),
    path('cart/', cart_view, name='cart'),
]
