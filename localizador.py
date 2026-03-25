cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
nome = input("digite o nome da sua cidade: ") 

if cidades in cidades:
    posiçao = cidades.index (nome)   
    print(f"A cidade {nome} está na posição {posição}") 

else: 
    print(f"A cidade {nome} não tem posição") 

