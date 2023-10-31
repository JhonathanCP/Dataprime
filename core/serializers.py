from rest_framework import serializers
from core.models import Clasificacion, TipoDeEntidad, Termino

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class TipoDeEntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeEntidad
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class TerminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termino
        extra_kwargs = {
            'definicion': {'required': False},
        }
        fields = '__all__'