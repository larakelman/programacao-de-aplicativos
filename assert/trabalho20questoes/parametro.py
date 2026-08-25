import sqlite3

def cadastrar_lista_alunos():
    lista = [("ana", 0), ("carlos", 1), ("beatriz", 3)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?,?)", lista)

    conexao.commit()
    conexao.close()

# a lista sempre começa de 0, 1, 2.. e não 1, 1, 2...
# tem que deixar (?, ?, ?) assim no cursor.execute por conta que na lista tem tres itens