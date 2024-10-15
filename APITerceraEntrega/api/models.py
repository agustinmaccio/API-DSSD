from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.username
