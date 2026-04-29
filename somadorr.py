def somar_carrinho(precos):
    total = 0
    
    # acumulador somando os preços
    for preco in precos:
        total += preco
    
    # aplica desconto se necessário
    if total > 500:
        total *= 0.9  # desconto de 10%
    
    return total


# Programa principal
carrinho = [120.50, 89.90, 300.00, 45.60]

valor_final = somar_carrinho(carrinho)

print(f"Valor final a pagar: R$ {valor_final:.2f}") 