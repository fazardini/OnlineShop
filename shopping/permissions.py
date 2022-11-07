from rest_framework.permissions import BasePermission


class IsProductCreator(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.created_by or request.user.is_superuser
