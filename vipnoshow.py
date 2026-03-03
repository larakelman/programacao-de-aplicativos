cliente = int(input("digite sua idade "))
ingresso = input("voce tem ingresso? S/N ")
nome_na_lista = input("seu nome esta na lista? S/N ") 

if cliente >= 18 and (ingresso == "S" or nome_na_lista == "S"): 
    print("seja bem vindo!")


