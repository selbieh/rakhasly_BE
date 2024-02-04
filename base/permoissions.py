
from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsAuthenticatedSuperuserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS are considered safe
            return True  # Allow read-only access for all users
        else:
            return request.user and (request.user.is_superuser or request.user.is_staff)  # Allow superusers and staff for write operations
