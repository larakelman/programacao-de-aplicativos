def contar_caracteres(texto): 
    return len(texto) 

#programa principal 
usuario = input("digite um nome de usuario: ")

tamanho = contar_caracteres(usuario)

if tamanho < 5: 
    print("nome de usuario muito curto")
else:
    print("nome aceito") 