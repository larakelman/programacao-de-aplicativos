import sqlite3
conexão = sqlite3.connect('escola_db')
cursor = conexão.cursor()
cursor.execute('''SELECT * FROM alunos ''')
todos_alunos = cursor.fetchall()

if not todos_alunos:
    print("nenhum aluno cadastrado")
else:
    for aluno in todos_alunos:
         print(f"ID: {aluno [0]}, nome: {aluno [1]} , telefone: {aluno [2]} , turma: {aluno [3]} , idade: {aluno [4]} , cpf:  {aluno [5]}") 

conexão.close()