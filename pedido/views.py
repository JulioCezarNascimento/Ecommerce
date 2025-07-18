from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse



class FinalizarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de finalizar o pedido")

class DetalhesPedido(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de detalhes do pedido")

class PagamentoPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Página de pagamento do pedido")
