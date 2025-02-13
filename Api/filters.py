import django_filters
from Api.models import Producto, Categoria, Venta, Cliente

class ProductoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')  
    categoria = django_filters.CharFilter(lookup_expr='icontains')  
    precio_min = django_filters.NumberFilter(field_name="precio", lookup_expr='gte')  
    precio_max = django_filters.NumberFilter(field_name="precio", lookup_expr='lte')  
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio_min', 'precio_max']

class CategoriaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Categoria
        fields = ['nombre']


class ventaFilter(django_filters.FilterSet):
    fecha = django_filters.DateFilter(field_name="Fechaventa", lookup_expr='exact')
    fecha_min = django_filters.DateFilter(field_name="fecha", lookup_expr='gte') 
    fecha_max = django_filters.DateFilter(field_name="fecha", lookup_expr='lte')

    class Meta:
        model = Venta
        fields = ['fecha', 'fecha_min', 'fecha_max']


class clienteFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')  
    direccion = django_filters.CharFilter(lookup_expr='icontains')  
    localidad = django_filters.CharFilter(lookup_expr='icontains')  
    telefono = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'localidad', 'telefono']