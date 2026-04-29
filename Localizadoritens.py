def esta_na_lista(lista, nome):
    for item in lista:
        if item == nome:
            return "encontrado"
        return " não disponivel"

    # Programa principal
frutas = ["maçã", "banana", "laranja", "uva"]

busca = input("Digite o nome da fruta: ")
resultado = esta_na_lista(frutas, busca)

print(resultado) 