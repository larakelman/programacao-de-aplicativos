import sqlite3

def cadastrar_serie(nome_serie, id_escola): 
    conexao = sqlite3.connect('escola_db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("erro: escola inexistente!")
    finally:
        conexao.close()

#faltou colocar o verificador de chave estrangeira 