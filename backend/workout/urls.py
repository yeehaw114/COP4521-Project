from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WorkoutsViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutsViewSet)
#router.register(r'sets', SetsViewSet)
#router.register(r'user_workouts', UserWorkoutsViewSet)
#router.register(r'user_sets', UserSetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]