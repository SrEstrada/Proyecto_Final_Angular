from django.db import models
from django.contrib.auth.models import AbstractUser

# USUARIO BASE PERSONALIZADO
class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('PACIENTE', 'Paciente'),
        ('MEDICO', 'Médico'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.username} ({self.tipo})"


# PACIENTE
class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_paciente')
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# MÉDICO
class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_medico')
    especialidad = models.CharField(max_length=100)
    cmp = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"Dr(a). {self.usuario.username} - {self.especialidad}"


# HORARIO GENERAL POR MÉDICO
class HorarioMedico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='horarios')

    def __str__(self):
        return f"Horario de {self.medico}"


# DÍA DE ATENCIÓN
class DiaAtencion(models.Model):
    DIAS = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
        ('SABADO', 'Sábado'),
        ('DOMINGO', 'Domingo'),
    ]
    horario_medico = models.ForeignKey(HorarioMedico, on_delete=models.CASCADE, related_name='dias')
    dia_semana = models.CharField(max_length=10, choices=DIAS)

    def __str__(self):
        return f"{self.dia_semana} - {self.horario_medico.medico}"


# HORAS DE ATENCIÓN
class HorarioAtencion(models.Model):
    dia_atencion = models.ForeignKey(DiaAtencion, on_delete=models.CASCADE, related_name='horas')
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin} ({self.dia_atencion.dia_semana})"


# RESERVACIONES
class Reservacion(models.Model):
    ESTADO_OPCIONES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='reservas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='reservas')
    horario = models.ForeignKey(HorarioAtencion, on_delete=models.CASCADE, related_name='reservaciones')
    fecha = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='PENDIENTE')

    def __str__(self):
        return f"{self.fecha} - {self.paciente} con {self.medico}"

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre