from django.shortcuts import render
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Produto, Pedido
from django.http import JsonResponse

# Create your views here.
def estatisticas_produtos(request):
    estatisticas = Produto.objects.aggregate(
        quantidade_produtos = Sum('quantidade_estoque'),
        preco_medio = Avg('preco'),
        maior_preco = Max('preco'),
        menor_preco = Min('preco'),
    )

    return JsonResponse(estatisticas)

def produtos_vendidos(request):
    produtos = Produto.objects.annotate(
        total_vendido = Sum('itens_pedido__quantidade'),
    )

    dados = list(produtos.values('id', 'nome', 'total_vendido'))

    return JsonResponse(dados, safe=False)

def pedidos_abertos(request):
    pedidos_abertos = Pedido.objects.abertos()

    return JsonResponse(pedidos_abertos, safe=False)
    