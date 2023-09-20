from django.contrib import admin
from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'category', 'description', 'price',)
    search_fields = ('name',)