# catalog/urls.py
from rest_framework.routers import DefaultRouter
from curso.views.curso import CursoViewSet


router = DefaultRouter()
router.register(r'categories', CursoViewSet, basename='Curso')


urlpatterns = router.urls
