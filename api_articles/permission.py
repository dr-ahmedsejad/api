from rest_framework.permissions import BasePermission
class IsRedacteur(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'redacteur'
class IsValidateur(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'validateur'

