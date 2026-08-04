import sqlite3

def criar_tabela():
    try: 
        conexao = sqlite3.connect('hospital.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON") 
            
        cursor.execute ("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
        ) """) 
        
        cursor.execute( cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm TEXT NOT NULL,
        id_hospital INTEGER NOT NULL,
        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )
        """)) 

        conexao.commit()
        conexao.close()
    
    except sqlite3.Error as erro: 
        print("erros ao criar a tabela:", erro) 
    finally:
        print("finalizado")

def criar_medico():
    try: 
        id_medico = int(input("digite o id do medico: "))
        nome = input("digite o nome do medico: ")
        crm = input("digite o crm do medico: ")
    except ValueError:
        print("erro: o ID deve ser um númeto inteiro valido: ")
    return 

conexao = sqlite3.connect('hospital.db')
cursor = conexao.cursor()


