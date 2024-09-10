from django.contrib import admin
from django.urls import include, path
from . import views
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('', include(router.urls)),
]
