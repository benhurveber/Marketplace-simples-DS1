from django.urls import path
from .views import estatisticas_produtos, produtos_vendidos, pedidos_abertos

urlpatterns = [
    path('estatisticas-produtos/', estatisticas_produtos, name='estatisticas_produtos'),
    path('produtos-vendidos/', produtos_vendidos, name='produtos_vendidos'),
    path('pedidos-abertos/', pedidos_abertos, name='pedidos_abertos')
]