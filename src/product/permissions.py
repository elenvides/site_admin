from rest_framework import exceptions
from rest_framework.permissions import BasePermission

from product.models import Product
from users.constants import Role


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER


class CanRemoveProduct(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN
