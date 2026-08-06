import sqlite3

def criar_tabelas():

    try: 
        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreing_keys = ON")
        cursor = conexao.cursor()


        cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        )''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS salas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_cinema INTEGER NOT NULL,
                        sala_cinema TEXT NOT NULL 
                        FOREIGN KEY (id_cinema) REFERENCES cinemas(id)
                        )''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("erro ao criar o banco: ", erro)

def inserir_tabelas():
    try: 
        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreign_keys = ON ")
        cursor = conexao.cursor 

        id_cinema = int(input("digite o nome do seu cinema: "))
        sala_cinema = int(input("digite sua sala do cinema: "))
        

