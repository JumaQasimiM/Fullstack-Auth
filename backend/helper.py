
from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsAdminCompanyJobSearchOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        
        # without login for evryone
        if request.method in SAFE_METHODS:
            return True
        
        # with login
        if not request.user or not request.user.is_authenticated:
            return False
        
        return request.user.role in ['admin', 'company','job_search']

