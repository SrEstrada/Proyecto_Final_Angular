from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadViewSet, listar_especialidades, medicos_por_especialidad

router = DefaultRouter()
router.register(r'especialidades', EspecialidadViewSet, basename='especialidad')

urlpatterns = [
    path('api/especialidades/', listar_especialidades),
    path('api/medicos/', medicos_por_especialidad),
    path('api/', include(router.urls)),
]