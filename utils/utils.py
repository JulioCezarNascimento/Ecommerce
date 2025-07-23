def formata_preco(value):
    """
    Formata o valor monetário para o padrão brasileiro (R$ 123,45).
    """
    return f'R$ {value:.2f}'.replace('.', ',')