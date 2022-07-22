from django.db import models

# Create your models here.

class Patrimonio(models.Model):

    nome_objeto = models.CharField(
        max_length=30,
        null=False,    # Não pode ser nulo
        blank=False    # Não pode ficar em branco
    )

    etiqueta = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    usuario = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    setor = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    dt_cadastro = models.DateField(
        
    )

    observacao = models.TextField(
        max_length=300
    )

    objetos = models.Manager()  



