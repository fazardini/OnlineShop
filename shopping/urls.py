from django.urls import path

from shopping.views import ProductList, DeleteProduct

urlpatterns = [
    path('products/', ProductList.as_view(), name='list_create_products'),
    path('products/<int:pk>/', DeleteProduct.as_view()),
]
