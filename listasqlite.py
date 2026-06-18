import sqlite3
conexao = sqlite3.connect('escola_db')
cursor = conexao.cursor()

def cadastrar_professor():
    nome = input("digite o nome do professor: ")
    telefone = input("digite o telefone do professor: ")
    materia = input("digite a materia do profesor: ")
    idade = int(input("digite a idade do professor: "))
    cpf = input("digite o cpf do professor: ")
    salario = input("digite o salario do professor: ")
    nome_escola = input("digite o nome da escola: ")

    cursor.execute (''' CREATE TABLE IF NOT EXISTS professores (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL , 
                    telefone TEXT , 
                    materia TEXT , 
                    idade INTEGER ,
                    cpf TEXT NOT NULL ,
                    salario REAL , 
                    nome_escola TEXT
                    )''')

    comando_inserir = f''' insert into professores (nome, telefone, materia, idade, cpf, salario, nome_escola)
                        VALUES ('{nome}', '{telefone}', '{materia}', {idade},'{cpf}', {salario}, '{nome_escola}') '''

    cursor.execute(comando_inserir) 
    conexao.commit()

def listar():
    cursor = conexao.cursor()
    cursor.execute(''' SELECT * FROM professores ''')
    todos_professores = cursor.fetchall()
    
    if not todos_professores: 
        print("nenhum professor cadastrado")
    else: 
        for professor in todos_professores:
            print(professor)
def atualizar():
    id_busca = int(input("deseja oque voce quer alterar: "))

    cursor.execute(f'''SELECT * FROM professores WHERE ID = {id_busca}''')
    professor = cursor.fetchone()

    if not professor:
        print: ("aluno não encontrado")
        return

    else:
        novo_nome = input("digite o novo nome do professor: ")
        novo_telefone = input("digite o novo telefone do professor: ")
        nova_materia = input("digite a nova materia do professor: ")
        nova_idade = int(input("digite a nova idade do profesor: "))
        novo_cpf = input("digite o novo cpf do professor: ")
        novo_salario = input("digite o novo salario do professor: ")
        nome_escola = input("digite a nova escola do professor: ")

        comando = f''' UPDATE professores SET nome = '{novo_nome}', telefone = '{novo_telefone}', materia = '{nova_materia}', idade = '{nova_idade}', cpf = '{novo_cpf}', salario = {novo_salario}, nome_escola = '{nome_escola}' WHERE ID = {id_busca}'''
        
        cursor.execute(comando)
        conexao.commit()

def excluir_professor(): 
    listar()  
    id_professor = int(input("digite o id do professor: "))

    cursor.execute(f''' DELETE FROM professores WHERE ID = {id_professor}''')
    conexao.commit()
    

def menu():
    opcao=0
    while opcao != 5:
        print("1- cadastrar_professor / 2 - listar / 3- atualizar / 4- exluir_professor / 5- sair")
        opcao = int(input("qual opcao vc deve escolher? "))

        if opcao == 1: cadastrar_professor()
        if opcao == 2: listar()
        if opcao == 3: atualizar()
        if opcao == 4: excluir_professor()
        if opcao == 5: 
            print("encerrando sistema")
            conexao.close() 
            return 
        else:
            print("opcao invalida")

    
menu()