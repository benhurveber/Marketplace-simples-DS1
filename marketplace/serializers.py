from rest_framework import serializers
from .models import Pedido, Produto, PerfilVendedor

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PerfilVendedorSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)
    class Meta:
        model = PerfilVendedor
        fields = ['id', 'cpf', 'data_nascimento', 'telefone', 'user', 'produtos']