nomes = ["lara", "melissa", "julia", "thauany", "christian"] 
verificar = input("digite seu numero de verificacao: ")

if verificar in nomes: 
    print(f"o nome {verificar} está na lista!")
else:
    print(f"o nome {verificar} não foi encontrado na lista")