import sqlite3

def buscar_professor(id_professor):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
resultado = cursor.fetchone()
print(resultado)
conexao.close()

#python não conseguer ler um parametro, por isso ele adiciona a virgula no final o parenteses entao ficara assim "(id_prof,)"