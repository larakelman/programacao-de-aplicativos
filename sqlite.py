import sqlite3 
conexão = sqlite3.connect('escola_db')
cursor = conexão.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL, 
                    telefone TEXT,
                    turma TEXT, 
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL
                    ) ''' ) 

nome_aluno = input("digite o nome do aluno: ")
telefone_aluno = input("digite o telfone do aluno: ")
turma_aluno = input("digite a turma do aluno: ")
idade_aluno = int(input("digite a idade do aluno: "))
cpf_aluno = input("digite o cpf do aluno: ")  

comando_inserir = (f''' 
                   INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                    VALUES ( ' {nome_aluno} ', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno} ', {cpf_aluno})''')

cursor.execute(comando_inserir)
conexão.commit()
conexão.close() 
