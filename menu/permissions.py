# to create a custom permission
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True # allowed to any one
        
        return request.user and request.user.is_staff
    
class IsAdminOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_authenticated 
    
class IsAdminOrDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name='Delivery Crew').exists()