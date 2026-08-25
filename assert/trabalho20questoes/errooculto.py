import sqlite3

def inserir_professor(nome, materia, cpf ):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)",
        (nome, materia, cpf))
        conexao.commit()
    except sqlite3.error: 
        print("erro: este CPF ja está cadastrando no sistema")
    finally:
        conexao.close()
        
# não é INSERTO no cursor.execute e sim INSERT 