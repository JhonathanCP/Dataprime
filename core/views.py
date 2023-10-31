from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from core.models import Clasificacion, TipoDeEntidad, Termino
from core.serializers import ClasificacionSerializer, TipoDeEntidadSerializer, TerminoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import connection


class ClasificacionRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer

class TipoDeEntidadRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = TipoDeEntidad.objects.all()
    serializer_class = TipoDeEntidadSerializer

class TerminoRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer