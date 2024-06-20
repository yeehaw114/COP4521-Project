from django.utils.deprecation import MiddlewareMixin
from django.db import connections
from django.conf import settings
import logging
from django.urls import resolve

logger = logging.getLogger(__name__)

class RoleBasedDatabaseMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = resolve(request.path_info).view_name
        excluded = ['RegistrationViewSet', ]
        # Check if the view is in the excluded views list
        if view_name in excluded:
            logger.info(f"Excluding view {view_name} from RoleBasedDatabaseMiddleware.")
            return None

        if request.user.is_authenticated:
            if request.user.role == 'Free':
                db_conn = connections['default']
                db_conn.settings_dict['USER'] = 'app_free'
                db_conn.settings_dict['PASSWORD'] = 'free_password'
                
            elif request.user.role == 'Premium':
                db_conn.settings_dict['USER'] = 'app_premium'
                db_conn.settings_dict['PASSWORD'] = 'premium_password'
            elif request.user.role == 'Admin':
                db_conn.settings_dict['USER'] = 'app_admin'
                db_conn.settings_dict['PASSWORD'] = 'admin_password'
            else:
                    db_conn = connections['default']
                    db_conn.settings_dict['USER'] = 'default_user'
                    db_conn.settings_dict['PASSWORD'] = 'default_password'