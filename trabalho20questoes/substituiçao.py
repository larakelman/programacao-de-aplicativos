import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):

    tabelas_permitidas = {"alunos", "professores", "disciplinas", "turmas"}
    if nome_tabela not in tabelas_permitidas:
        raise ValueError(f"Acesso negado para a tabela: {nome_tabela}")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?", (id_registro,))
    
    print(cursor.fetchone())
    conexao.close()



   # O SQLite rejeita o caractere ? na posição do nome da tabela, disparando um erro de sintaxe.
   # A string com a instrução do banco de dados foi inserida incorretamente dentro do método conexao.cursor().