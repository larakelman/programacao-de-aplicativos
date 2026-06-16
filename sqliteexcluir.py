import sqlite3

def deletar():
    
    conexao = sqlite3.connect("escola_db")
    cursor = conexao.cursor()

    id_aluno = int(input("digite o nome do id que voce deseja deletar: "))
    cursor.execute(f'''SELECT id FROM Alunos WHERE Id = {id_aluno}''')
    aluno = cursor.fetchone()

if not aluno: 
    print ("o aluno não foi encontrado ")

else:
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("o aluno foi deletado")

        conexao.close() 
