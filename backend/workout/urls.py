from django.urls import path
from . import views

urlpatterns = [
    path('user/create', views.addUser),
    path('user/<str:pk>', views.getUser)
]