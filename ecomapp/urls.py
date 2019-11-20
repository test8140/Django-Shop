from django.urls import path
from ecomapp.views import base_view

urlpatterns = [
    path('', base_view, name='base'),
]
