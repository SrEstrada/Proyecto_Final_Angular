from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register_user
from .views import reservar_cita

from .views import (
    listar_especialidades,
    crear_especialidad,
    editar_especialidad,
    eliminar_especialidad,
    medicos_por_especialidad
)

urlpatterns = [
    path('especialidades/', listar_especialidades),           # GET
    path('especialidades/crear/', crear_especialidad),        # POST
    path('especialidades/<int:pk>/editar/', editar_especialidad),  # PUT/PATCH
    path('especialidades/<int:pk>/eliminar/', eliminar_especialidad),  # DELETE
    path('medicos/', medicos_por_especialidad),
    path('register/', register_user, name='api_register'),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('citas/reservar/', reservar_cita, name='api_reservar_cita'),
]