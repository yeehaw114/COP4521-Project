from rest_framework.routers import SimpleRouter
from workouts.views import SetsViewSet, UserWorkoutsViewSet, UserSetsViewSet, WorkoutsViewSet

workout_router = SimpleRouter()

workout_router.register(r'workouts', WorkoutsViewSet, basename='workouts')
workout_router.register(r'sets', SetsViewSet, basename='sets')
workout_router.register(r'user-workouts', UserWorkoutsViewSet, basename='user-workouts')
workout_router.register(r'user-sets', UserSetsViewSet, basename='user-sets')
