from django.contrib import admin
from .models import Usuario, Paciente, Medico, HorarioMedico, DiaAtencion, HorarioAtencion, Reservacion

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(HorarioMedico)
admin.site.register(DiaAtencion)
admin.site.register(HorarioAtencion)
admin.site.register(Reservacion)
