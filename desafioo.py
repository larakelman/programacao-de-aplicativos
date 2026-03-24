autorizacao = ["alice", "bob", "carlos"] 
usuario = input("digite o nome de um pesquisador: ") 

if usuario in autorizacao:
    print(f"acesso permitido! o pesquisador {usuario} está na posição" , autorizacao.index(usuario))

    lista = input("deseja remover esse pesquisador da lista? sim/não: ")
    if lista == "sim": 
        autorizacao.remove(usuario) 
        print(f"lista atualizadas {autorizacao}")

    else: 
        print("acesso encerrado")

else:
    print(f"acesso negado! o pesquisador {usuario} não foi encontrado ")

    cadastrar = input("deseja cadastrar esse novo pesquisador? sim/nao: ")
    if cadastrar == "sim":
        autorizacao.append("usuario") 