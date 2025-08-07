def conteudo_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    
    total_itens_carrinho = sum(
        [item['quantidade'] for item in carrinho.values()]
    )
    
    return {
        'total_itens_carrinho': total_itens_carrinho,
    }