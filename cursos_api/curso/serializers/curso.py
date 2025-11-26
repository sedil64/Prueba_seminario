# catalog/serializers/category.py
from rest_framework import serializers
from curso.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("id","codigo","titulo","subtitulo","descripcion","nivel","duracion_horas","costo","modalidad","fecha_inicio","estado","created_at","updated_at")
        read_only_fields = ("id","created_at","updated_at")
        
        
