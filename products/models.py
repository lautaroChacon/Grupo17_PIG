from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, default="nada" ,verbose_name="Descripcion")
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    #falta agregar imagen
    #falta agregar stock

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']