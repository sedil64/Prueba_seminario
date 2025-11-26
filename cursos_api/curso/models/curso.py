# catalog/models/category.py
from django.db import models

class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=120, unique=True)
    titulo = models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120)
    nivel = models.CharField(max_length=120)
    duracion_horas = models.IntegerField()
    costo = models.IntegerField()
    modalidad = models.CharField(max_length=120)
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name
