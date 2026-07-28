def menu():
    while True:
        print("1. Cadastrar aluno")
        print("2. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == '1':
            print("Cadastrando...")
            
        elif opcao == '2':
            print("Saindo do programa...")
            break  
        
        else:
            print("Opção inválida. Tente novamente.")
            
                 break

# o comando pass no encerramento não faz nada, para fechar o menu, é necessário usar o comando break.
# a função print e input estavam sem aspas nos textos,  o Python não reconhece palavras soltas sem aspas.