from django.db import models

# Create your models here.
class Clasificacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Termino(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    definicion = models.TextField(blank=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Indicador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    definicion = models.TextField(blank=True)
    medida = models.TextField(blank=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class BaseDeDatos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)

    def __str__(self):
        return self.nombre
    
class Tabla(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    basesDeDatos = models.ManyToManyField(BaseDeDatos, blank=True)

    def __str__(self):
        return self.nombre
    
class Columna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    tablas = models.ManyToManyField(Tabla, blank=True)

    def __str__(self):
        return self.nombre
    
class Visualizacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    tablasDeEntrada = models.ManyToManyField(Tabla, blank=True)
    url = models.TextField(null=True, blank=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    
    def __str__(self):
        return self.nombre

class Proceso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    tablasDeEntrada = models.ManyToManyField(Tabla, related_name='tablas_entrada', blank=True)
    tablasDeSalida = models.ManyToManyField(Tabla, related_name='tablas_salida', blank=True)
    clasificaciones = models.ManyToManyField(Clasificacion, blank=True)
    
    def __str__(self):
        return self.nombre