from rest_framework import permissions


class Moder(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class Owner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            return False
