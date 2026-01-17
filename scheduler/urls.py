from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LearningTaskViewSet
from .views import register
from django.urls import path
from .views import create_admin



router = DefaultRouter()
router.register(r'tasks', LearningTaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
     path('register/', register),
      path("create-admin/", create_admin),
]