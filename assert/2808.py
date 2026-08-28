import sqlite3

nome_banco = "escola.db"

def conectar():
    def conectar():
    try:
        conexao = sqlite3.connect(NOME_BANCO)
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        raise


def criar_tabelas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especialidade TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS disciplinas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                professor_id INTEGER NOT NULL,
                FOREIGN KEY (professor_id)
                    REFERENCES professores(id)
                    ON DELETE RESTRICT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                disciplina_id INTEGER NOT NULL,
                nota REAL DEFAULT 0,
                FOREIGN KEY (aluno_id)
                    REFERENCES alunos(id)
                    ON DELETE CASCADE,
                FOREIGN KEY (disciplina_id)
                    REFERENCES disciplinas(id)
                    ON DELETE CASCADE,
                UNIQUE(aluno_id, disciplina_id)
            )
        """)

        conexao.commit()
        conexao.close()
