from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from curso.serializers.curso import CursoSerializer
from curso.models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [AllowAny]