from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from auth.urls import auth_router
from user.views import UserViewSet

router = DefaultRouter()
router.registry.extend(auth_router.registry)
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include((router.urls, 'api'))),
]