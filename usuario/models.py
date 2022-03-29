import email
from wsgiref.validate import validator
from django.db import models
from django.core.validators import EmailValidator

class UsuarioModel(models.Model):
    email = models.CharField(
        db_column="EMAIL",
        max_length=60,
        validator = EmailValidator()
    )

    senha = models.CharField(
        db_column="SENHA",
        max_length=12,
    )
