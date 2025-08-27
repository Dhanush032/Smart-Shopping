from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Permission to only allow owners of an object or admin to access it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Admin users have full access
        if request.user.is_authenticated and request.user.is_admin:
            return True
        
        # Users can only access their own objects
        return obj.user == request.user

class IsAdminOrOwner(BasePermission):
    """
    Permission for admin users or object owners
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.user == request.user