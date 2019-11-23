from django.urls import path
from ecomapp.views import base_view, category_view, product_view

urlpatterns = [
    path('', base_view, name='base'),
    path('category/<str:slug>', category_view, name="category_detail"),
    path('product/<str:slug>', product_view, name="product_detail"),
]
