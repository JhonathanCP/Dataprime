from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from core.models import Clasificacion, Termino, Indicador, BaseDeDatos, Tabla, Columna, Visualizacion, Proceso
from core.serializers import ClasificacionSerializer, TerminoSerializer, IndicadorSerializer, BaseDeDatosSerializer, TablaSerializer, ColumnaSerializer, VisualizacionSerializer, ProcesoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import connection


class ClasificacionRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer

class TerminoRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer

class IndicadorRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class BaseDeDatosRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = BaseDeDatos.objects.all()
    serializer_class = BaseDeDatosSerializer

class TablaRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Tabla.objects.all()
    serializer_class = TablaSerializer

class ColumnaRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer

class VisualizacionRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer

class ProcesoRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer