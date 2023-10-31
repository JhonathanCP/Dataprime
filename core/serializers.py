from rest_framework import serializers
from core.models import Clasificacion, Termino, Indicador, BaseDeDatos, Tabla, Columna, Visualizacion, Proceso

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
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

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        extra_kwargs = {
            'definicion': {'required': False},
        }
        fields = '__all__'

class BaseDeDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseDeDatos
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class ColumnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columna
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class VisualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualizacion
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        extra_kwargs = {
            'descripcion': {'required': False},
        }
        fields = '__all__'