nome_cliente = input("digite o seu nome: ")
valor_total_compra = float(input("digite o valor total da compra: "))
entrega = int(input("qual a distancia da entrega: "))
cupom = input("digite o cupom: ")
frete = 40.00 

if valor_total_compra >= 1000.00 and cupom == "s": 
    subtracao = valor_total_compra * 0.20
    total = valor_total_compra - desconto 
    print("parabens! voce ganhou um mousepad de brinde")

elif valor_total_compra > 500.00 and valor_total_compra < 1000.00 and cupom == "s":
    desconto = valor_total_compra * 0.10
    total = valor_total_compra - desconto 
elif entrega <= 50 and valor_total_compra > 200.00: 
    frete = 0.00 

print("nome cliente:" , nome_cliente)
print("valor total compra:" , valor_total_compra)
print("valor desconto:" , cupom)
print("valor final a pagar:" , valor_total_compra)


