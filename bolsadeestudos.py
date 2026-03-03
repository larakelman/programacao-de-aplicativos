media = float(input("digite sua media "))
renda = float(input("digite sua renda familiar "))
escola = input("voce veio de escola publica? S/N") 

if media >= 8.0 and (renda < 2.000 or escola == "S"):
    print("ganhou a bolsa")

else: 
    print("nao atende os requisitos") 
