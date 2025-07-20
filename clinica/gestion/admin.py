from django.contrib import admin
from .models import Especialidad, Medico, Paciente, Cita ,Horario

admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Horario)