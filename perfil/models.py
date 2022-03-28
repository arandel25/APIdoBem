from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class PerfilModel(models.Model):
    nome_instituicao = models.CharField(
        db_column="NOME_INSTITUICAO",
        max_length=50,
        null=True,
    )

    cnpj = models.CharField(
        db_column="CNPJ",
        max_length=14,
        validators=[MinLengthValidator(14), MaxLengthValidator(14)],
        null=True,
    )

    logradouro = models.CharField(
        db_column="LOGRADOURO",
        max_length=20,
        null=True,
    )

    numero = models.CharField(
        max_length=4,
        null=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(4)],
    )

    complemento = models.CharField(
        db_column="COMPLEMENTO",
        max_length=20,
        null=True,
    )

    bairro = models.CharField(
        db_column="BAIRRO",
        max_length=20,
        null=True,
    )

    municipio = models.CharField(
        db_column="MUNICIPIO",
        max_length=20,
        null=True,
    )

    uf = models.CharField(
        db_column="UF",
        max_length=2,
        null=True,
    )

    cep = models.CharField(
        db_column="CEP",
        max_length=8,
        validators=[MinLengthValidator(8), MaxLengthValidator(8)],
        null=True,
    )

    telefone = models.CharField(
        db_column="TELEFONE",
        max_length=11,
        validators=[MinLengthValidator(10), MaxLengthValidator(11)],
        null=True,
    )

    ano_fundacao = models.CharField(
        db_column="ANO_FUNDACAO",
        max_length=4,
        validators=[MinLengthValidator(4), MaxLengthValidator(4)],
        null=True,
    )

    total_membros = models.PositiveIntegerField(
        db_column="TOTAL_MEMBROS",
        null=True,
    )

    nome_presidente_instituicao = models.CharField(
        db_column="NOME_PRESIDENTE_INSTITUICAO",
        max_length=50,
        null=True,
    )

    class Meta:

        db_table = "PERFIL"

        verbose_name = "perfil"

        verbose_name_plural = "perfis"


    def __str__(self) -> str:

        return self.nome_instituicao