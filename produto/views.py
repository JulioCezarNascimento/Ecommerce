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
        http_referer = request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )

        variacao_id = request.GET.get('vid')

        if not variacao_id:
            messages.error(request, 'Produto não existe.')
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if variacao.estoque < 1:
            messages.error(request, 'Estoque insuficiente.')
            return redirect(http_referer)

        if not request.session.get('carrinho'):
            request.session['carrinho'] = {}
            request.session.save()

        carrinho = request.session['carrinho']

        if variacao_id in carrinho:
            quantidade_carrinho = carrinho[variacao_id]['quantidade']
            quantidade_carrinho += 1

            if variacao.estoque < quantidade_carrinho:
                messages.warning(
                    request,
                    f'Estoque insuficiente para {quantidade_carrinho}x no '
                    f'produto "{variacao.produto.nome}". Adicionamos '
                    f'{variacao.estoque}x no seu carrinho.'
                )
                quantidade_carrinho = variacao.estoque

            carrinho[variacao_id]['quantidade'] = quantidade_carrinho

        else:
            carrinho[variacao_id] = {
                'quantidade': 1,
            }

        request.session.save()
        messages.success(
            request,
            f'Produto "{variacao.produto.nome} ({variacao.nome})" adicionado ao seu carrinho.'
        )

        return redirect(http_referer)

class RemoveProduto(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Página de remover produto")

class Carrinho(View):
    """Exibe o carrinho de compras."""
    def get(self, request, *args, **kwargs):
        carrinho = request.session.get('carrinho', {})
        variacao_ids = carrinho.keys()

        variacoes = list(models.Variacao.objects.select_related('produto').filter(id__in=variacao_ids))

        for variacao in variacoes:
            vid = str(variacao.id)
            variacao.quantidade_carrinho = carrinho[vid]['quantidade']
            
            
            preco_unitario = variacao.preco_promocional if variacao.preco_promocional > 0 else variacao.preco
            variacao.preco_quantitativo = preco_unitario * variacao.quantidade_carrinho

        contexto = {
            'variacoes_carrinho': variacoes
        }

        return render(request, 'produto/carrinho.html', contexto)
class FinalizarCompra(View):
    def get(self,request ,*args, **kwargs):
        return HttpResponse("Página de Finalizar compra")
