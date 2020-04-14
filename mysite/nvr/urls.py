from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("groups", views.GroupViewSet)


urlpatterns = [
    path('index', views.index),
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    path('concatenate', views.concatenate),
]
