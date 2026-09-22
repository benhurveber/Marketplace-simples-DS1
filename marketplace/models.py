from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PerfilVendedor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.firstname

class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
            return self.nome   

class Produto(models.Model):
    vendedor = models.ForeignKey (
        PerfilVendedor,
        on_delete=models.CASCADE
        related_name='produtos'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='produtos'
    )

    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
            return self.nome

class Pedido(models.Model):
    

class ItemPedido(models.Model):
    pedido