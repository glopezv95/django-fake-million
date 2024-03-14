from django.urls import path, include
from rest_framework import routers

from .views import ClientModelViewSet, count

router = routers.DefaultRouter()
router.register('apiviewset', ClientModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/count/', count, name = 'count')
]