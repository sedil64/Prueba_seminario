from django.urls import path, include
from rest_framework.routers import DefaultRouter
from curso.views.curso import CursoViewSet
from curso.views.reportes import horas_semanales
from curso.views.aprobacion import aprobacion

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reportes/horas-semanales', horas_semanales),
    path('reportes/aprobacion', aprobacion),
]
