from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAdmin(BasePermission):
    message = "Admin Access is required"
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.role=="ADMIN")

class IsAdminOrManager(BasePermission):
    message = "Admin or Manager access required."
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.role in ["ADMIN", "MANAGER"])

class IsAdminManagerOrEmployee(BasePermission):
    message = "Admin or Manager or Employee access required."
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and request.user.role in ["ADMIN", "MANAGER", "EMPLOYEE"])