from django.utils.deprecation import MiddlewareMixin
from django.db import connections, connection
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
import logging
import json
from django.urls import resolve
from user.models import User       
from django.db import connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication


logger = logging.getLogger(__name__)

class RoleBasedDatabaseMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        db_conn = connections['default']
        role = None
        # Get the view name
        view_name = resolve(request.path_info).view_name
        logger.debug(f'View name: {view_name}')
        
        # Check if the view is in the excluded views list
        if view_name == 'api:auth-register-list' or view_name == 'api:auth-login-list' or view_name == 'api:auth-refresh-list':
            db_conn.settings_dict['USER'] = 'postgres'
            db_conn.settings_dict['PASSWORD'] = 'postgres'
            return
        # Get username from token
        auth_header = request.headers.get('Authorization')
        logger.debug(f'Authorization header: {auth_header}')
        tokenString = ""
        if auth_header:
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(auth_header.split()[1])
                tokenString = str(jwt_auth.get_user(validated_token))
            except (InvalidToken, TokenError) as e:
                logger.error(f'Invalid token: {e}')

        # Extract substring containing 'username=jim'
        start_index = tokenString.find("username=") + len("username=")
        end_index = tokenString.find(")", start_index)
        uname = tokenString[start_index:end_index]
        with connection.cursor() as cursor:
            cursor.execute("SELECT role FROM user_user WHERE username = %s;", [uname])
            result = cursor.fetchone()
            role = result[0]

        # Set the appropriate database user based on role
        if role == 'Free':
            db_conn.settings_dict['USER'] = 'app_free'
            db_conn.settings_dict['PASSWORD'] = 'free_password'
            logger.debug('Switched to app_free user')
        elif role == 'Premium':
            db_conn.settings_dict['USER'] = 'app_premium'
            db_conn.settings_dict['PASSWORD'] = 'premium_password'
            logger.debug('Switched to app_premium user')
        elif role == 'Admin':
            db_conn.settings_dict['USER'] = 'app_admin'
            db_conn.settings_dict['PASSWORD'] = 'admin_password'
            logger.debug('Switched to app_admin user')
        else:
            return None
