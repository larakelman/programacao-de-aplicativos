import sqlite3 
conexao = sqlite3.connect('escola_db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL, 
                    telefone TEXT,
                    turma TEXT, 
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    id_professor INTEGER NOT NULL, 

                    FOREIGN KEY (id_professor) REFERENCES professores (ID)
                    ) ''' ) 

def criar():
    print("\n ====CADASTRAR ALUNOS ====")
    nome_aluno = input("digite o nome do aluno: ")
    telefone_aluno = input("digite o telfone do aluno: ")
    turma_aluno = input("digite a turma do aluno: ")
    idade_aluno = int(input("digite a idade do aluno: "))
    cpf_aluno = input("digite o cpf do aluno: ")  

    id_professor = int(input("qual o id do professor?: "))

    comando_inserir = (f''' 
                    INSERT INTO alunos (nome, telefone, turma, idade, cpf, id_professor)
                        VALUES ( ' {nome_aluno} ', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno} ', {cpf_aluno}, {id_professor})''')

    cursor.execute(comando_inserir)
    conexao.commit()

def ver_alunos():
    cursor.execute(" SELECT * FROM alunos ")
    alunos = cursor.fetchall() 
    print("\n ==== ALUNOS REGISTRADOS ===")
    for aluno in alunos:
        print(aluno)

def atualizar_alunos():
    ver_alunos()
    print("\n === VER ALUNOS ===")
    
    idx = int(input("qual id voce deseja mudar: "))

    cursor.execute( 
        "SELECT * FROM alunos WHERE id = ? ", (idx,)
    )
    aluno = cursor.fetchone()

    if aluno:
        nome_aluno = input("digite o nome do aluno: ")
        telefone_aluno = input("digite o telfone do aluno: ")
        turma_aluno = input("digite a turma do aluno: ")
        idade_aluno = int(input("digite a idade do aluno: "))
        cpf_aluno = input("digite o cpf do aluno: ")  

        cursor.execute(
            f"UPDATE alunos SET nome = '{nome_aluno}', telefone = '{telefone_aluno}', turma = '{turma_aluno}', idade = '{idade_aluno}', cpf = '{cpf_aluno}' WHERE id = {idx}"
        )
    
        conexao.commit() 
        print("aluno alterado com sucesso!")
    
    else:
        print("aluno não encontrado! ")

def deletar_aluno():
    print("\n === DELETAR ALUNO === ")
    ver_alunos() 
    idx = int(input("qual aluno vc deseja deletar: "))

    cursor.execute(
        f''' DELETE FROM alunos WHERE id = {idx}'''
    )
    conexao.commit()
    print("aluno removido com sucesso!")

def menu():
    opcao = 0
    while opcao != 5:
        print("\n === MENU ===")
        print("1- criar alunos / 2- ver alunos / 3- atualizar alunos / 4- deletar aluno / 5- sair ")
        opcao = int(input("qual opcao vc vai escolher?: "))
        
        if opcao ==1: criar()
        elif opcao ==2: ver_alunos()
        elif opcao ==3: atualizar_alunos()
        elif opcao ==4: deletar_aluno()
        elif opcao ==5: 
            conexao.close() 
            break 

menu()