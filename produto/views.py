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
       produto = variacao.produto
       
       produto_id = produto.id
       produto_nome = produto.nome
       variacao_nome = variacao.nome or ''
       variacao_id = variacao.id
       preco_unitario = variacao.preco
       preco_unitario_promocional = variacao.preco_promocional
       quantidade = 1
       slug = produto.slug 
       imagem = variacao.imagem 
       
       if imagem:
           imagem = settings.MEDIA_URL + str(imagem)
       else:
           imagem = settings.STATIC_URL + 'img/produto-sem-imagem.png'
       
       if variacao.estoque < 1:
           messages.error(
               self.request, 
               'Produto fora de estoque.'
           )
           return redirect(http_referer)
       
       if not self.request.session.get('carrinho'):
           self.request.session['carrinho'] = {}
           self.request.session.save()
           
       carrinho = self.request.session['carrinho']
       
       if variacao_id in carrinho:
           quantidade_carrinho = carrinho[variacao_id]['quantidade']
           quantidade_carrinho += 1
           
           if quantidade_carrinho > variacao.estoque:
               messages.error(
                   self.request, 
                   'Quantidade solicitada fora de estoque.'
               )
               return redirect(http_referer)
           
           carrinho[variacao_id]['quantidade'] = quantidade_carrinho
           carrinho[variacao_id]['preco_quantiativo'] = preco_unitario * quantidade_carrinho
        
       else:
           carrinho[variacao_id] = {
               'produto_id': produto_id,
               'produto_nome': produto_nome,
               'variacao_nome': variacao_nome,
               'variacao_id': variacao_id,
               'preco_unitario': preco_unitario,
               'preco_unitario_promocional': preco_unitario_promocional,
               'preco_quantiativo': preco_unitario * quantidade,
               'preco_quantiativo_promocional': preco_unitario_promocional * quantidade,
               'quantidade': quantidade,
               'slug': slug,
               'imagem': imagem
           }
           
           self.request.session.save()
      
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
