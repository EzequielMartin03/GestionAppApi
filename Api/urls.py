from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, VentaViewSet, CategoriaViewSet, ClienteViewSet
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = DefaultRouter()

router.register('productos', ProductoViewSet)
router.register('ventas', VentaViewSet)
router.register('categorias', CategoriaViewSet)
router.register('clientes', ClienteViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentación",
        default_version="v1",
        description="Documentación de la API de productos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ezequielnmartin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
    

)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentación",
        default_version="v1",
        description="Documentación de la API con Swagger UI",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

urlpatterns = [
    path('', include(router.urls)),
    # Ruta para obtener el token (login)
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Ruta para renovar el token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

