def calcular_desconto(preco, porcentual):
    return preco - (preco * porcentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

assert calcular_desconto(1000, 15) == 850

print("todos os testes se passaram!")

# O erro era que a função subtraía o percentual diretamente do preço, em vez de calcular o valor correspondente à porcentagem.


