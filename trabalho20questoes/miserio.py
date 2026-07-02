import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   cpf TEXT
                )
            ''')
    
    cursor.execute(
        "INSERT INTO professores (nome, cpf) VALUES (?, ?)",
        (nome, cpf)
    )

    conexao.commit()
    conexao.close()



# o erro era por que o cpf não estava unique e ele so pode ser unico 
# entao para não dar erro tem que colocar unique no cpf
