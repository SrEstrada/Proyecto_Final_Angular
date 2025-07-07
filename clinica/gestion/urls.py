from django.urls import path
from .views import listar_especialidades, medicos_por_especialidad

urlpatterns = [
    path('api/especialidades/', listar_especialidades),
    path('api/medicos/', medicos_por_especialidad),
]