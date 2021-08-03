from .views import CursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CursoViewSet, basename='cursos')

urlpatterns = [
]

urlpatterns += router.urls