from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('Adicionar', views.AddProduto.as_view(), name='AddProduto'),
    path('Remover', views.RemoveProduto.as_view(), name='RemoveProduto'),
    path('Carrinho', views.Carrinho.as_view(), name='Carrinho'),
    path('FinalizarCompra', views.FinalizarCompra.as_view(), name='FinalizarCompra'),
]
