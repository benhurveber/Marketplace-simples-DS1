from django.contrib import admin
from .models import PerfilVendedor, PerfilCliente, Tag, Pedido, Produto, ItemPedido

# Register your models here.
@admin.register(PerfilVendedor)
class PerfilVendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'data_nascimento', 'telefone')

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'data_nascimento', 'telefone')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendedor', 'nome', 'descricao', 'preco', 'quantidade_estoque')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido', 'status')

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'produto', 'quantidade', 'preco_venda')