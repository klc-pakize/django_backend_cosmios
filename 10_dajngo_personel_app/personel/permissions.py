from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_staff)
    

    # def has_permission(self, request, view):
    #     SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    #     if request.method in SAFE_METHODS:
    #         return True
    #     return bool(request.user and request.user.is_staff)


