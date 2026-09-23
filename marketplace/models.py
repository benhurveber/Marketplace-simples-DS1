from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PerfilVendedor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_vendedor'
    )
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Perfil vendedor'
        verbose_name_plural = 'Perfis vendedores'

class PerfilCliente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_cliente'
    )
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.first_name 

    class Meta:
        verbose_name = 'Perfil cliente'
        verbose_name_plural = 'Perfis clientes'

class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
            return self.nome   

class Produto(models.Model):
    vendedor = models.ForeignKey (
        PerfilVendedor,
        on_delete=models.CASCADE,
        related_name='produtos'
    )
    tags = models.ManyToManyField (
        Tag,
        blank=True,
        related_name='produtos'
    )

    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
            return self.nome

class Pedido(models.Model):
    class Status(models.TextChoices):
         ABERTO = 'aberto', 'Aberto'
         CONFIRMADO = 'confirmado', 'Confirmado'
         CANCELADO = 'cancelado', 'Cancelado'

    cliente = models.ForeignKey(
         PerfilCliente,
         on_delete=models.CASCADE,
         related_name='pedidos'
    )

    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
         max_length=15, choices=Status.choices, default=Status.ABERTO
    )

    def __str__(self):
         return f'Pedido nº {self.id} feito por {self.cliente}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(
         Pedido,
         on_delete=models.CASCADE,
         related_name='itens_pedido'

    )

    produto = models.ForeignKey(
         Produto,
         on_delete=models.CASCADE,
         related_name='itens_pedido'
    )

    quantidade = models.IntegerField()
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2, editable=False)

    class Meta:
        verbose_name = 'Item pedido'
        verbose_name_plural = 'Itens pedido'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.preco_venda = self.produto.preco

        super().save(*args, **kwargs)
