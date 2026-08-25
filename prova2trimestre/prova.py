import sqlite3
conexao = sqlite3.connect('hospital_db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON") 

def criar_tabela():
        cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS redes_hospitalares (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                grupo_medico TEXT NOT NULL,
                registro_ans TEXT NOT NULL
            )
            ''') 

        cursor.execute('''CREATE TABLE IF NOT EXISTS medicos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_hospital TEXT NOT NULL,
               id_rede INTEGER NOT NULL,
               FOREIGN KEY (id_rede) REFERENCES redes_hospitalares (id)
            )
            ''')
        
    
def criar_hospital():
    print("\=====CADASTRAR HOSPITAL=====")
    id = input("digite o id do hospital: ")
    nome_hospital = input("digite o nome do hospital: ")
    id_rede = input("digite a rede do hospital: ")

    comando_inserir = (f''' INSERT INTO hospitais (id, nome_hospital, id_rede)
                       VALUES ('{id}', '{nome_hospital}', '{id_rede}')''')
    
    cursor.execute(comando_inserir)
    conexao.commit()

def ver_medicos():
      cursor.execute("SELECT * FROM medicos")
      medicos = cursor.fetchall()
      print("\===== MEDICOS CADASTRADOS=====")
      for medico in medicos:
            print(f"ID: {medico[0]} | NOME_HOSPITAL: {medico[1]} | ID_REDE: {medico[2]}")

def atualizar_medicos():
        ver_medicos()
        print("\=====ATUALIZAR MEDICOS =====")

        idx = int(input(digite oque voce quer mudar: ))

        cursor.execute(
                    "SELECT * FROM medicos WHERE id = ? ", (idx,)
                   )
        medico = cursor.fetchone
    
        if medico:
              id = int(input("digite o novo id do medico: "))
              grupo_medico = int(input("digite o novo grupo medico: "))
              registro_ans = int(input("digite o novo registro_ans do medico: "))

        cursor.execute(
              f"UPDATE medicos SET id = '{id}', grupo medico = '{grupo_medico}', registro_ans = '{registro_ans}' WHERE id = {idx}"
             ) 
        
        conexao.commit()
    print("medico alterado com sucesso: ")






