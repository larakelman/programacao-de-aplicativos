import sqlite3 

def cadastrar_escola_manual(): 

    try:
        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 
    except ValueError:
        print("Erro: O ID deve ser um número inteiro válido.")
        return 

    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 

    try:
        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
        conexao.commit()
        print("Escola cadastrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: O ID digitado já está em uso por outra escola.")
    finally:
        conexao.close()


#Se um ID já cadastrado fosse digitado de novo, o banco gerava um erro (sqlite3.IntegrityError) 
#Quando o codigo buga no INSERT, o comando conexao.close() nunca era executado, travando o arquivoS. 
# Se o usuário digitasse uma letra em vez de número, o int(input()) quebrava o script na hora.