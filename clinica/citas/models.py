from django.db import models
from django.contrib.auth.models import User

class Cita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medico} - {self.fecha} {self.hora}"
