nota_teste = int(input("digite a sua nota: "))
possui_certificacao = input("tem a certificação? sim/nao: ")
anos_xp = int(input("digite quantos anos de experiencia: "))

def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    if (nota_teste > 80 and anos_xp >= 2) or possui_certificacao == "sim":
        print("contrater")
    else:
        print("descartar")

resultado = verificar_aprovacao(nota_teste, anos_xp, possui_certificacao)
    