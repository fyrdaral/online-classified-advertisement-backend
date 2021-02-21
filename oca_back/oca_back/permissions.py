from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated):
            return True
        return False


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as an admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAuthenticatedOrReadCreateOnly(BasePermission):
    """
    The request is authenticated as an admin / same user, or is a read-only and create request.
    """
    def has_permission(self, request, view):
        if (request.method in ['GET', 'HEAD', 'OPTIONS', 'POST']) or (request.user and
                request.user.is_authenticated and (
                view.kwargs['pk'] == request.user.id or request.user.is_staff)):
            return True
        return False
