from django.urls import path
from .views import (
    listar_especialidades,
    crear_especialidad,
    editar_especialidad,
    eliminar_especialidad,
    medicos_por_especialidad
)

urlpatterns = [
    path('api/especialidades/', listar_especialidades),           # GET
    path('api/especialidades/crear/', crear_especialidad),        # POST
    path('api/especialidades/<int:pk>/editar/', editar_especialidad),  # PUT/PATCH
    path('api/especialidades/<int:pk>/eliminar/', eliminar_especialidad),  # DELETE
    path('api/medicos/', medicos_por_especialidad),
]