from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from core.models import Clasificacion, Termino, Indicador, BaseDeDatos, Tabla, Columna, Visualizacion, Proceso
from core.serializers import ClasificacionSerializer, TerminoSerializer, IndicadorSerializer, BaseDeDatosSerializer, TablaSerializer, ColumnaSerializer, VisualizacionSerializer, ProcesoSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class ClasificacionRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer


class TerminoRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este término.")
        return super().retrieve(request, *args, **kwargs)

class IndicadorRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este indicador.")
        return super().retrieve(request, *args, **kwargs)

class BaseDeDatosRetrieveUpdateDestroyView(ModelViewSet):
    queryset = BaseDeDatos.objects.all()
    serializer_class = BaseDeDatosSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta base de datos.")
        return super().retrieve(request, *args, **kwargs)

class TablaRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Tabla.objects.all()
    serializer_class = TablaSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta tabla.")
        return super().retrieve(request, *args, **kwargs)

class ColumnaRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta columna.")
        return super().retrieve(request, *args, **kwargs)

class VisualizacionRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta visualización.")
        return super().retrieve(request, *args, **kwargs)

class ProcesoRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este proceso.")
        return super().retrieve(request, *args, **kwargs)