def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

print(" os testes passaram!")

# A função original estava subtraindo o percentual diretamente do preço, o erro foi corrigido calculando primeiro o valor do desconto 
# exemplo, 20% de R$ 200 é R$ 40, então o preço final é R$ 160.

