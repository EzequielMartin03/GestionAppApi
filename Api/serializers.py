from rest_framework import serializers
from Api.models import Producto, Categoria, Venta, Cliente
from django.db import transaction

class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio','categoria', 'color', 'stock']

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
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
        fields = ['id', 'productos', 'cantidad', 'fecha', 'cliente']

    def validate(self, data):
        productos = data.get('productos', [])
        cantidad = data.get('cantidad', 0)

        # Verifica si hay suficiente stock de cada producto
        for producto in productos:
            if producto.stock < cantidad:
                raise serializers.ValidationError(f'No hay suficiente stock para el producto {producto.nombre}.')

        return data

    def create(self, validated_data):
        with transaction.atomic():
            productos = validated_data.pop('productos')  
            cantidad = validated_data['cantidad']

            venta = Venta.objects.create(**validated_data)  
            venta.productos.set(productos)  

            for producto in productos:
                if producto.stock < cantidad:
                    raise serializers.ValidationError(f'No hay suficiente stock para el producto {producto.nombre}.')

                producto.stock -= cantidad
                producto.save()

        return venta

