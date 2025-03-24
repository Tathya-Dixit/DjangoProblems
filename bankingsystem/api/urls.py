from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import APIViewSet

router = DefaultRouter()
router.register(r'api', APIViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
]