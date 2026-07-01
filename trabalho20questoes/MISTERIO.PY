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



# A função cria a tabela "professores", mas não insere os dados recebidos para o "nome" e "cpf
# Está faltando o comando INSERT INTO para colocar o professor na tabela 
# adicionar o conexao.commit() para salvar as alterações e conexao.close() para fechar a conexão no banco de dados