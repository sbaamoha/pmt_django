from rest_framework import routers
from django.urls import path, include
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
