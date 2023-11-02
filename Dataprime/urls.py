"""Dataprime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from core.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserListView, UserDetailView
from authentication.views import UserRegistrationView, UserUpdateRoleView, CustomTokenObtainPairView

router = routers.DefaultRouter()
router.register(r'clasificacion', ClasificacionRetrieveUpdateDestroyView, 'clasificacion')
router.register(r'termino', TerminoRetrieveUpdateDestroyView, 'termino')
router.register(r'indicador', IndicadorRetrieveUpdateDestroyView, 'indicador')
router.register(r'base-de-datos', BaseDeDatosRetrieveUpdateDestroyView, 'base-de-datos')
router.register(r'tabla', TablaRetrieveUpdateDestroyView, 'tabla')
router.register(r'columna', ColumnaRetrieveUpdateDestroyView, 'columna')
router.register(r'visualizacion', VisualizacionRetrieveUpdateDestroyView, 'visualizacion')
router.register(r'proceso', ProcesoRetrieveUpdateDestroyView, 'proceso')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/update-role/', UserUpdateRoleView.as_view(), name='user-update-role'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]