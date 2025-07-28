from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib import messages
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
   


class Adicionar(View):
   def get(self, request, *args, **kwargs):
       http_referer = self.request.META.get(
           'HTTP_REFERER',
           reverse('produto:lista')
           )
       variacao_id = request.GET.get('vid')
       
       if not variacao_id:
           messages.error(
               self.request, 
               'Selecione uma variação do produto.'
            )
           return redirect(http_referer)
       
       variacao = get_object_or_404(models.Variacao, id=variacao_id)
       
       
       return HttpResponse(f'{variacao.produto.nome} {variacao.nome} adicionado ao carrinho!')


class RemoveProduto(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de remover produto")


class Carrinho(View):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de carrinho de compras")


class FinalizarCompra(View):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de Finalizar compra")
