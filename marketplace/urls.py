from django.urls import path, include
from .views import estatisticas_produtos, produtos_vendidos, pedidos_abertos, ProdutoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('estatisticas-produtos/', estatisticas_produtos, name='estatisticas_produtos'),
    path('produtos-vendidos/', produtos_vendidos, name='produtos_vendidos'),
    path('pedidos-abertos/', pedidos_abertos, name='pedidos_abertos'),
    path('', include(router.urls)),
]