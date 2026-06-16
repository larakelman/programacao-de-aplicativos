import sqlite3
conexao = sqlite3.connect('escola_db')
cursor = conexao.cursor()

def cadastrar_professor():
    nome = input("digite o nome do professor: ")
    materia = input("digite a materia do profesor: ")
    idade = int(input("digite a idade do professor: "))
    cpf = input("digite o cpf do professor: ")
    salario = input("digite o salario do professor: ")
    nome_escola = input("digite o nome da escola: ")

    cursor.execute (
                    ''' CREATE TABLE IF NOT pofessores (ID INTEGER PRIMARY KEY AUTO INCREMENT, 
                    nome TEXT NOT NULL , 
                    materia TEXT , 
                    idade INTEGER ,
                    cpf TEXT UNIQUE NOT NULL ,
                    salario TEXT , 
                    nome_escola TEXT 
                    )''') 
    comando_inserir = f''' insert into professores (nome, materia, idade, cpf, salario, nome_escola)
    VALUIS (' {nome} ', {materia} ' , {idade} ' , {cpf} ' , {salario} ' , {nome_escola}) '''

    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
cursor.execute('''SELECT * FROM alunos''') 