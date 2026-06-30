import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno: ")

try:
    id_turma = int(input("digite o ID numerico da turma: "))

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome,
 id_turma))
except ValueError: 
    conexao.commit()
except sqlite3.eror:
    print("erro no banco de dados")
finally:
        if 'conexao' in locals:
             conexao.close()

#faltou adicionar um excepet que é "except ValueError:"
        
       
        
    
