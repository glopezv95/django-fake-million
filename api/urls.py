from django.urls import path, include
from rest_framework import routers

from .views import ClientModelViewSet, count, login

router = routers.DefaultRouter()
router.register('apiviewset', ClientModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/count/', count, name = 'count'),
    path('api/login/', login, name = 'login'),
]