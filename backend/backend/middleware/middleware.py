from django.db import connections
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class RoleBasedDatabaseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            role = request.user.role.name  # Assuming user has a role attribute
            if role in settings.DATABASE_ROLES:
                db_role = settings.DATABASE_ROLES[role]
                connections['default'].settings_dict['USER'] = db_role['USER']
                connections['default'].settings_dict['PASSWORD'] = db_role['PASSWORD']
