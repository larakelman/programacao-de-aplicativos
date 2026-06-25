import sqlite3
conexao = sqlite3.connect('escola_db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT
)
''') 

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT,
    cidade TEXT,
    estado TEXT
)
""")

conexao.commit() 

def cadastrar_professor():
    conexao = sqlite3.connect("escola.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO professor (nome, telefone, endereco) VALUES (?, ?, ?)",
        (nome, telefone, endereco)
    )

    conexao.commit()
    conexao.close() 