from django.utils.deprecation import MiddlewareMixin
from django.db import connections
from django.conf import settings

class RoleBasedDatabaseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            role = getattr(request.user, 'role', None)  # Assuming role is a CharField
            if role and role in settings.DATABASE_ROLES:
                db_role = settings.DATABASE_ROLES[role]
                connection = connections['default']
                connection.settings_dict['USER'] = db_role['USER']
                connection.settings_dict['PASSWORD'] = db_role['PASSWORD']
