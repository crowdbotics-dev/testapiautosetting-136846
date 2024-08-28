from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136846ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136846", Testconnectors136846ViewSet, basename="testconnectors136846"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
