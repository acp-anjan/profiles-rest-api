from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow users to update"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profiles"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id  


class PostOwnStatus(permissions.BasePermission):
    """allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id 