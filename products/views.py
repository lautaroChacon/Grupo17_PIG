from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'