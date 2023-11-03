from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from core.dbConnection import DBConnection
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
from rest_framework import filters


class ClasificacionRetrieveUpdateDestroyView(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

class TerminoRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Termino.objects.all()
    serializer_class = TerminoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este término.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class IndicadorRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este indicador.")
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class BaseDeDatosRetrieveUpdateDestroyView(ModelViewSet):
    queryset = BaseDeDatos.objects.all()
    serializer_class = BaseDeDatosSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta base de datos.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class TablaRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Tabla.objects.all()
    serializer_class = TablaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta tabla.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class ColumnaRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta columna.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class VisualizacionRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a esta visualización.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

class ProcesoRetrieveUpdateDestroyView(ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'clasificaciones__nombre']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        for clasificacion in instance.clasificaciones.all():
            if clasificacion not in user_clasificaciones:
                raise PermissionDenied("No tienes permiso para acceder a este proceso.")
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Lógica de verificación de clasificaciones aquí
        user_clasificaciones = request.user.clasificaciones.all()
        queryset = self.filter_queryset(self.get_queryset())
        filtered_queryset = [term for term in queryset if all(clasificacion in user_clasificaciones for clasificacion in term.clasificaciones.all())]
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
class FillEntitiesFromDB(APIView):
    def post(self, request, format=None):
        # Obtén el nombre de la base de datos desde el request
        database_name = request.data.get('database_name')

        try:
            database_entity = BaseDeDatos.objects.get(nombre=database_name)
        except BaseDeDatos.DoesNotExist:
            # Si no existe, crea una nueva entidad de tipo "Base de datos"
            database_entity = BaseDeDatos.objects.create(nombre=database_name)

        source_connection = DBConnection(database=database_name)
        source_cursor = source_connection.cursor()


        # Obtén las tablas de la base de datos externa
        source_cursor.execute(
            f"SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_catalog='{database_name}'")

        source_tables = source_cursor.fetchall()

        for source_table in source_tables:
            table_name = source_table[0]
            try:
                table_entity = Tabla.objects.get(nombre=table_name)
            except Tabla.DoesNotExist:
                # Si no existe, crea una nueva entidad de tipo "Tabla"
                table_entity = Tabla.objects.create(nombre=table_name)
                table_entity.basesDeDatos.add(database_entity)
            else:
                # Si ya existe, verifica si el fathers ya está presente
                if database_entity not in table_entity.basesDeDatos.all():
                    table_entity.basesDeDatos.add(database_entity)

            # Obtén las columnas de la tabla
            source_cursor.execute(
                f"SELECT column_name FROM information_schema.columns WHERE table_name='{table_name}' AND table_catalog='{database_name}'")

            source_columns = source_cursor.fetchall()

            for source_column in source_columns:
                column_name = source_column[0]
                try:
                    column_entity = Columna.objects.get(nombre=column_name)
                except Columna.DoesNotExist:
                    # Si no existe, crea una nueva entidad de tipo "Columna"
                    column_entity = Columna.objects.create(nombre=column_name)
                    column_entity.tablas.add(table_entity)
                else:
                    # Si ya existe, verifica si el fathers ya está presente
                    if table_entity not in column_entity.tablas.all():
                        column_entity.tablas.add(table_entity)

        source_cursor.close()
        source_connection.close()
        return Response(status=201)
    
class ColumnView(APIView):
    def get(self, request, id):
        # column_name = request.data.get('column_name')  # Obtener el nombre de la columna desde el parámetro de consulta
        column = Columna.objects.get(id = id)#, entityType__id=3)
        father_table = column.tablas.first()
        father_table = Columna.objects.get(id=father_table.id)
        father_database = father_table.tablas.first()
        father_database = Columna.objects.get(id=father_database.id)
        source_connection = DBConnection(database=father_database.name)
        source_cursor = source_connection.cursor()
        # Obtén las tablas de la base de datos externa
        source_cursor.execute(f"SELECT column_name, is_nullable, data_type, character_maximum_length, numeric_precision, numeric_scale, datetime_precision FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{father_table.name}' AND column_name = '{column.name}'")
        columns_info = source_cursor.fetchall()
        for row in columns_info:
            column_name = row[0]
            is_nullable = row[1]
            data_type = row[2]
            character_maximum_length = row[3]
            numeric_precision = row[4]
            numeric_scale = row[5]
            datetime_precision = row[6]

        # Crear un diccionario con la información de la columna
        column_info = {
            'column_name': column_name,
            'is_nullable': is_nullable,
            'data_type': data_type,
            'character_maximum_length': character_maximum_length,
            'numeric_precision': numeric_precision,
            'numeric_scale': numeric_scale,
            'datetime_precision': datetime_precision,
            }
        serializer = ColumnaSerializer(column)
        combined_data = {**column_info, **serializer.data}
        source_cursor.close()
        source_connection.close()
        return JsonResponse(combined_data, status = 201)

class TableView(APIView):
    def get(self, request, id):
        father_table = Tabla.objects.get(id=id)
        father_database = father_table.basesDeDatos.first()

        source_connection = DBConnection(database=father_database.nombre)
        source_cursor = source_connection.cursor()

        # Obtener la información de las columnas de la tabla
        source_cursor.execute(
            f"SELECT column_name, is_nullable, data_type, character_maximum_length, numeric_precision, numeric_scale, datetime_precision FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{father_table.name}'"
        )
        columns_info = source_cursor.fetchall()
        column_info_list = []

        for row in columns_info:
            column_name = row[0]
            is_nullable = row[1]
            data_type = row[2]
            character_maximum_length = row[3]
            numeric_precision = row[4]
            numeric_scale = row[5]
            datetime_precision = row[6]
            entity = Tabla.objects.get(nombre=column_name)
            column_id = entity.id

            column_info = {
                'column_name': column_name,
                'is_nullable': is_nullable,
                'data_type': data_type,
                'character_maximum_length': character_maximum_length,
                'numeric_precision': numeric_precision,
                'numeric_scale': numeric_scale,
                'datetime_precision': datetime_precision,
                'column_id': column_id,
            }

            column_info_list.append(column_info)

        # Obtener los nombres de las columnas de la tabla
        column_names = [column['column_name'] for column in column_info_list]

        # Obtener el data sample de la tabla
        source_cursor.execute(f"SELECT * FROM {father_table.nombre} LIMIT 20")
        data_sample = source_cursor.fetchall()

        # Convertir los resultados en una lista de diccionarios
        data_sample_list = []
        for row in data_sample:
            row_dict = dict(zip(column_names, row))
            data_sample_list.append(row_dict)

        source_cursor.close()
        source_connection.close()

        serializer = TablaSerializer(father_table)

        response_data = {
            'entity': serializer.data,
            'column_info_list': column_info_list,
            'data_sample': data_sample_list
        }

        return JsonResponse(response_data, status=201)
    
class AddInputTable(APIView):
    def patch(self, request, id):
        try:
            process = Proceso.objects.get(id=id)
        except Proceso.DoesNotExist:
            raise NotFound("Proceso no encontrado")

        input_table_id = request.data.get('input_table_id')

        if not input_table_id:
            return JsonResponse({'error': 'Debe proporcionar el ID de la tabla de entrada'}, status=400)

        try:
            input_table = Tabla.objects.get(id=input_table_id)
        except Tabla.DoesNotExist:
            return JsonResponse({'error': 'Tabla de entrada no encontrada'}, status=404)

        process.tablasDeEntrada.add(input_table)
        serializer = ProcesoSerializer(process)

        return Response(serializer.data, status=200)


class RemoveInputTable(APIView):
    def patch(self, request, id):
        try:
            process = Proceso.objects.get(id=id)
        except Proceso.DoesNotExist:
            raise NotFound("Proceso no encontrado")

        input_table_id = request.data.get('input_table_id')

        if not input_table_id:
            return JsonResponse({'error': 'Debe proporcionar el ID de la tabla de entrada'}, status=400)

        try:
            input_table = Tabla.objects.get(id=input_table_id)
        except Tabla.DoesNotExist:
            return JsonResponse({'error': 'Tabla de entrada no encontrada'}, status=404)

        process.tablasDeEntrada.remove(input_table)
        serializer = ProcesoSerializer(process)

        return Response(serializer.data, status=200)


class AddOutputTable(APIView):
    def patch(self, request, id):
        try:
            process = Proceso.objects.get(id=id)
        except Proceso.DoesNotExist:
            raise NotFound("Proceso no encontrado")

        output_table_id = request.data.get('output_table_id')

        if not output_table_id:
            return JsonResponse({'error': 'Debe proporcionar el ID de la tabla de salida'}, status=400)

        try:
            output_table = Tabla.objects.get(id=output_table_id)
        except Tabla.DoesNotExist:
            return JsonResponse({'error': 'Tabla de salida no encontrada'}, status=404)

        process.tablasDeSalida.add(output_table)
        serializer = ProcesoSerializer(process)

        return Response(serializer.data, status=200)


class RemoveOutputTable(APIView):
    def patch(self, request, id):
        try:
            process = Proceso.objects.get(id=id)
        except Proceso.DoesNotExist:
            raise NotFound("Proceso no encontrado")

        output_table_id = request.data.get('output_table_id')

        if not output_table_id:
            return JsonResponse({'error': 'Debe proporcionar el ID de la tabla de salida'}, status=400)

        try:
            output_table = Tabla.objects.get(id=output_table_id)
        except Tabla.DoesNotExist:
            return JsonResponse({'error': 'Tabla de salida no encontrada'}, status=404)

        process.tablasDeSalida.remove(output_table)
        serializer = ProcesoSerializer(process)

        return Response(serializer.data, status=200)