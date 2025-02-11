from django.db import models

class Categoria (models.Model):
    Nombre = models.CharField(max_length=50)
    
   
    
class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Color = models.CharField(max_length=50)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, related_name="venta")
    cantidad = models.IntegerField()
    fecha = models.DateField()




   
    