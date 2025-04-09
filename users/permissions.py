from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Manager'

class IsSalesAgent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Agent'

class IsCEO(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'CEO'
