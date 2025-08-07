from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('adicionar/', views.Adicionar.as_view(), name='adicionar'),
    path('remover/', views.RemoveProduto.as_view(), name='removeProduto'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar-compra/', views.FinalizarCompra.as_view(), name='finalizarcompra'),

    path('<slug:slug>/', views.DetalheProduto.as_view(), name='detalhe'),
]