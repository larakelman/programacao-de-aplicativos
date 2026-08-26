def calcular_frete(valor):
    return valor >= 200

def pode_votar(idade):
    return idade >= 16

def senha_invalida(senha):
    return len(senha) >= 8

assert calcular_frete(199.99) == False
assert calcular_frete(200) == True
assert calcular_frete(200.01) == True

assert pode_votar(15) == False 
assert pode_votar(16) == True 
assert pode_votar(17) == True

assert senha_invalida(1234567) == False
assert senha_invalida(12345678) == True 
assert senha_invalida(123456789) == True

# o objetivo era criar testes para verificar os valores de cada def, ate o seu limite, para testar antes e depois deles.
