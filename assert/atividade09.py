def buscar_nome(lista, nome):
    return nome in lista 

def ter_senha_valida(senha):
    return len(senha) >= 8

assert buscar_nome(["lara, bianca"], "emily") == True
assert buscar_nome([], "lara") == False
assert buscar_nome(["lara"], "lara") == True 


assert ter_senha_valida("12345678") == True
assert ter_senha_valida("") == False
assert ter_senha_valida("abc123") == False


print("Todos os testes passaram!")
