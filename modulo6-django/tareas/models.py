from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente','Pendiente'),
        ('en_progreso','En progreso'),
        ('completada','Completada'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    