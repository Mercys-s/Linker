from rest_framework import permissions


class IsAuthorOrDenied (permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return bool (request.user.is_authenticated)

        else: # request.user.username == obj.user or 
            if  request.user.username == obj.author or \
                request.user.is_staff:
                return True
                
    