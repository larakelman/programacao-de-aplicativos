import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON; ")

    cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", 
                    (nome, id_serie, id_prof))
    
    conexao.commit()
    conexao.close()

# a consulta INSERT possui 3 colunas (nome_turma, id_serie e id_professor), mas apenas 2 integorração (?, ?) no comando VALUES 