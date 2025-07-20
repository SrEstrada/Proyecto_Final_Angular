from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register_user
from .views import reservar_cita
from .views import perfil_paciente, citas_paciente
from .views import admin_pacientes_list_create, admin_paciente_detail

from .views import (
    listar_especialidades,
    crear_especialidad,
    editar_especialidad,
    eliminar_especialidad,
    medicos_por_especialidad,
    horarios_por_medico
)

urlpatterns = [
    path('especialidades/', listar_especialidades),           # GET
    path('especialidades/crear/', crear_especialidad),        # POST
    path('especialidades/<int:pk>/editar/', editar_especialidad),  # PUT/PATCH
    path('especialidades/<int:pk>/eliminar/', eliminar_especialidad),  # DELETE
    path('medicos/', medicos_por_especialidad),
    path('horarios/', horarios_por_medico),
    path('register/', register_user, name='api_register'),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('citas/reservar/', reservar_cita),
    path('paciente/perfil/', perfil_paciente, name='api_perfil_paciente'),
    path('paciente/citas/', citas_paciente, name='api_citas_paciente'),
    path('admin/pacientes/', admin_pacientes_list_create, name='api_admin_pacientes'),
    path('admin/pacientes/<int:pk>/', admin_paciente_detail, name='api_admin_paciente_detalle'),
]