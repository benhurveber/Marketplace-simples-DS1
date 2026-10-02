from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pedido

@receiver(post_save, sender=Pedido)
def notificar_pedido_confirmado(sender, instance, created, **kwargs):
    if instance.status == Pedido.Status.CONFIRMADO:
        for objeto_item in instance.itens_pedido.all():
            produto = objeto_item.produto
            produto.quantidade_estoque -= objeto_item.quantidade
            produto.save()