def aplicar_promocao(precos):
    nova_lista = []
    
    for preco in precos:
        if preco > 100:
            preco *= 0.85  # desconto de 15%
        nova_lista.append(preco)
    
    return nova_lista


# Programa principal
compras = [150.0, 80.0, 200.0, 50.0]
atualizada = aplicar_promocao(compras)

print("Lista original:", compras)
print("Lista com desconto:", atualizada) 