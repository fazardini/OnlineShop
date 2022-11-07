from django.urls import path

from shopping.views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
]
