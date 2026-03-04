valor_total = float(input("Digite o valor total da compra: "))
cliente = input("voce é prime?: ")
frete = 50.0

if valor_total >= 500.00 or (cliente == "sim" and valor_total >= 100.00): 
    print("parabens! voce ganhou frete gratis")
    frete = 0.0
    print("valor" , valor_total)

valor_final = valor_total + frete
print("valor" , valor_final) 

