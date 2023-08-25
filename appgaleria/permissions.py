from rest_framework import permissions

class IsCoupleOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the couple to edit/approve it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Se for um método "seguro" (por exemplo, GET), permita
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Se o usuário pertencer ao grupo "Couple", permita
        return request.user.groups.filter(name='Couple').exists()
