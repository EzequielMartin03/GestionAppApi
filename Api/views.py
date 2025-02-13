from .models import Categoria, Producto, Venta, Cliente
from .serializers import ProductoSerializer,VentaSerializer,CategoriaSerializer,ClienteSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import ProductoFilter, ventaFilter, clienteFilter, CategoriaFilter

from rest_framework.permissions import IsAuthenticated

from .permissions import Admin, Empleado, EsEmpleadoOAdmin
class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsEmpleadoOAdmin]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductoFilter
    ordering_fields = ['nombre', 'precio']

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, Admin]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CategoriaFilter
    ordering_fields = ['nombre']

class VentaViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsEmpleadoOAdmin]
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ventaFilter
    ordering_fields = ['fecha', 'fecha_min', 'fecha_max']

class ClienteViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsEmpleadoOAdmin]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = clienteFilter
    ordering_fields = ['nombre', 'direccion', 'localidad', 'telefono']
   
   