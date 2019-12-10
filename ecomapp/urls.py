from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from ecomapp.views import (
    base_view, category_view, 
    product_view, add_to_cart_view, 
    cart_view, remowe_from_cart_view, 
    change_item_qty, checkout_view,
    order_create_view, make_order_view, 
    account_view, registration_view,
    login_view,
    )

urlpatterns = [
    path('', base_view, name='base'),
    path('category/<str:slug>', category_view, name='category_detail'),
    path('product/<str:slug>', product_view, name='product_detail'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
    path('remowe_from_cart/', remowe_from_cart_view, name='remowe_from_cart'),
    path('change_item_qty/', change_item_qty, name='change_item_qty'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('order/', order_create_view, name='create_order'),
    path('thank_you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you'),
    path('account/', account_view, name='account'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('base')), name='logout'),
]   
 