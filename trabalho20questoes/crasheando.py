import sqlite3

def cadastrar_serie_seguro(nome, id_escola): 
    try:  
        conexao = sqlite3.connect('sistema.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))
    except sqlite3.error as e:
        print("erro técnico:", e)
    if conexao: 
        conexao.close()


# deu erro por conta que o conexao poderia dar erro por conta do finally vai fechar alguma coisa que vai dar erro
# adicionmos if conexao: