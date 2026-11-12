from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminOrManagerOrReadOnly(permissions.BasePermission):
    """
    Lettura per tutti gli autenticati.
    Scrittura solo per staff/admin o utenti del gruppo 'Gestori'.
    """

    def _is_admin_or_manager(self, user):
        return bool(
            user and user.is_authenticated and (
                user.is_staff or
                user.groups.filter(name='Gestori').exists()
            )
        )

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return self._is_admin_or_manager(request.user)

    def has_object_permission(self, request, view, obj):
        # Lettura consentita
        if request.method in permissions.SAFE_METHODS:
            return True
        # Scrittura consentita solo ad admin/staff o Gestori
        return self._is_admin_or_manager(request.user)
