from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if view.action == "create":
            return True
        article = view.get_object()
        return article.author_id == user.id
        #     return True
        # return False


class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if view.action == 'create':
            user = view.get_object()
            return request.user.id == user.id

