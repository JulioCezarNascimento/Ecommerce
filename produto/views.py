from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from . import models

class ListaProdutos(ListView):
   model = models.Produto
   template_name = 'produto/lista_produtos.html'
   context_object_name = 'produtos'
   paginate_by = 10

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe_produto.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
   


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
