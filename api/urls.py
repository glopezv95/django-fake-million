from django.urls import path

from . import views

urlpatterns = [
    path('api/login/', views.login, name = 'login'),
    path('api/count/', views.count, name = 'count'),
]