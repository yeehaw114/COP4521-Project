from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import permission_required
from guardian.shortcuts import assign_perm

# Assign a user to a role
user = User.objects.get(username='cooldog')
admin_group = Group.objects.get(name='admin')
admin_group.user_set.add(user)

@permission_required('auth.add_user', raise_exception=True)
def create_user(request):
    # Your view logic
    print("hello!")
    pass

@permission_required('auth.change_user', raise_exception=True)
def edit_user(request):
    # Your view logic
    print("hello! 2!")
    pass

def assign_permissions(request, user, obj):
    assign_perm('auth.change_user', user, obj)

def check_permissions(request, user, obj):
    if user.has_perm('auth.change_user', obj):
        # logic
        pass

# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     http_method_names = ['get']
#     serializer_class = UserSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['modified']
#     ordering = ['-modified']
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.all()
#         return User.objects.filter(id=self.request.user.id)