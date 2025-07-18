from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('FinalizarCompra/', views.FinalizarPedido.as_view(), name='FinalizarCompra'),
    path('DetalhesPedido/', views.DetalhesPedido.as_view(), name='DetalhesPedido'),
    path('PagamentoPedido/', views.PagamentoPedido.as_view(), name='PagamentoPedido'),
]
