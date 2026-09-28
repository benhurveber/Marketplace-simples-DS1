from django.urls import path
from .views import estatisticas_produtos, produtos_vendidos

urlpatterns = [
    path('estatisticas-produtos/', estatisticas_produtos, name='estatisticas_produtos'),
    path('produtos-vendidos/', produtos_vendidos, name='produtos_vendidos')
]