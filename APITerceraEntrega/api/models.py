from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    # cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    fecha = models.DateTimeField()  # Fecha del pedido
    data = models.JSONField()  # Almacenamos el JSON con los materiales

    # def __str__(self):
    #     return f'Pedido de {self.cliente} en {self.fecha}'