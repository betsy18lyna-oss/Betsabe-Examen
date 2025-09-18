from django.utils import timezone
from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=150)
    estreno = models.DateTimeField(default=timezone.now)
    anio = models.IntegerField(default=2025)

    def __str__(self):
        return self.nombre
