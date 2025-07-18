from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
import sys 

class ListaProdutos(ListView):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de listar produtos")


class DetalheProduto(View):
    def get(self, reqest, *args, **kwargs):
        return HttpResponse("Página de detalhes do pedido")


class AddProduto(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de adicionar produto")


class RemoveProduto(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de remover produto")


class Carrinho(View):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de carrinho de compras")


class FinalizarCompra(View):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de Finalizar compra")
