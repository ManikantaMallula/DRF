from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)

        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGetorPatch(BasePermission):
    def has_permission(self, request, view):
        allow = ['GET', 'PATCH']

        if request.method in allow:
            return True

        else:
            return False



class Alex(BasePermission):
    def has_permission(self, request, view):

        username = request.user.username
        print(username)


        if username.lower() == 'alex':
            return True

        elif username != '' and len(username)%2 == 0 and request.method in SAFE_METHODS:
            return True

        else:
            return False


