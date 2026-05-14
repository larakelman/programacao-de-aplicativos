open("viagens.txt", 'w').close() 

def criar():
    destino = input("para onde deseja viajar")
    with open ("viagens.txt" , 'a') as arquivo:
        arquivo.write(destino+ '\n' )
    print("destino encontrado") 

def ler():
    with open("viagens.txt", 'r') as arquivo: 
        viagens = arquivos.readlines() 

    i = 0 
    for viagem in viagens:
        print(f"{i} - {viagens.strip()}")
        i += 1

def atualizar():
    ler()
    idx = int(input("digite seu destino que deseja alterar: "))
    novo_destino = input("novo destino:" )

    with open('viagens.txt', 'r') as arquivos:
        linhas = arquivos.readlines()

    linhas[idx] = novo_destino + '\n' 

    with open ('viagens.txt' , 'w') as arquivos:
        arquivos.writelines(linhas)
    print("destino atualizado!") 

def deletar():
    ler()
    idx = int(input("digite o destino que deseja excluir")) 


    with open ('viagens.txt', 'r') as arquivos:
        linhas = arquivos.readlines()

    del linhas[idx] 

    with open ('viagens.txt' , 'w') as arquivos:
        arquivos.writelines(linhas)
    print(destino removido!)

while True: 
     print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
     opcao = input("escolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break 