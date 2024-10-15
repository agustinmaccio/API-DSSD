from django.contrib.auth.models import AbstractUser
from django.db import models

class Pedido(models.Model):
    # cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    fecha = models.DateTimeField()  # Fecha del pedido
    data = models.JSONField()  # Almacenamos el JSON con los materiales
class CustomUser(AbstractUser):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.username
