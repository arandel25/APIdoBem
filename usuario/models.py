from django.contrib.auth.models import AbstractUser
from django.db import models
from perfil.models import PerfilModel

class UsuarioModel(AbstractUser):
    perfil = models.OneToOneField(
        PerfilModel,
        models.CASCADE,
        null=True
    )

    username = models.EmailField(
        unique=True
    )