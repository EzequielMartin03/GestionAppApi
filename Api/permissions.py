from rest_framework.permissions import BasePermission

class Admin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()

class Empleado(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Empleado').exists()


class EsEmpleadoOAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.groups.filter(name='Empleado').exists() or 
            request.user.groups.filter(name='Admin').exists()
        )
