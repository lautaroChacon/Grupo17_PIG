from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('product-list/', ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail'),
]
