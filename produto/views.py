from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
   model = models.Produto
   template_name = 'produto/lista_produtos.html'
   context_object_name = 'produtos'
   paginate_by = 10

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
