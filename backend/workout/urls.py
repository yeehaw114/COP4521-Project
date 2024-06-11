from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet, SetViewSet, UserWorkoutViewSet, UserSetViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet)
router.register(r'sets', SetViewSet)
router.register(r'user_workouts', UserWorkoutViewSet)
router.register(r'user_sets', UserSetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]