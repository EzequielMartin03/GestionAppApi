
from rest_framework import serializers
from Api.models import Producto, Categoria, Venta, Cliente
class ProductoSerializer(serializers.ModelSerializer):
    
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
   
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio','categoria']

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value
    
    def validate_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError("El stock debe ser mayor o igual a 0.")
        return value

    def validate_categoria(self, value):
        if value is None:
            raise serializers.ValidationError("La categoría es obligatoria.")
        return value
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'Nombre']
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'direccion', 'localidad', 'telefono']

class VentaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'productos', 'cantidad', 'fecha']



