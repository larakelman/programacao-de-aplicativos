rua = int(input("digite o número da rua: "))
numero = int(input("digite seu numero: "))
bairro = input("digite o bairro: ")
cidade = input("digite a cidade")
cep = int(input("digite o cep: ")) 

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"rua {rua}, Nº {numero}, bairro {bairro}, cep {cep} e cidade {cidade}"

informacoes = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print(informacoes) 