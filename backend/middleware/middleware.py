from django.utils.deprecation import MiddlewareMixin
from django.db import connections
from django.conf import settings
import logging
import json
from django.urls import resolve
from user.models import User       
from django.db import connections


logger = logging.getLogger(__name__)

class RoleBasedDatabaseMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        role = None
        if request.user.is_authenticated:
            role = user.role

        # Check for Role in query parameters
        role = request.GET.get('role', None)
        
        # Check for Role in form data (for POST requests)
        if not role:
            role = request.POST.get('role', None)
        
        # Check for Role in JSON data (for POST/PUT requests with JSON body)
        if not role:
            try:
                body_data = json.loads(request.body)
                role = body_data.get('role', None)  # None is the default if 'role' is not found
            except (json.JSONDecodeError, TypeError):
                pass

        logger.debug(f'Role from request: {role}')
        
        # Fetch role from the database if not provided in the request and user is authenticated
        if role == None:
            try:
                # Log the username and primary key for debugging
                logger.debug(f'Attempting to retrieve user with primary key: {request.user.pk} and username: {request.user.username}')
                
                # Fetch the user from the database using the primary key or username
                user = User.objects.get(pk=request.user.pk)
                # Alternatively, use username if needed
                # user = User.objects.get(username=request.user.username)

                # Access the role attribute of the user object
                role = user.role
                logger.debug(f'Role from database: {role}')
            except User.DoesNotExist:
                logger.error(f'User with primary key {request.user.pk} or username {request.user.username} does not exist.')
                role = None

        logger.debug(f'Final role: {role}')
        
        # Get the view name
        view_name = resolve(request.path_info).view_name
        logger.debug(f'View name: {view_name}')
        
        
        db_conn = connections['default']


        # Check if the view is in the excluded views list
        if view_name == 'api:auth-register-list':
            return
        
        elif role == 'Free':
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
            return