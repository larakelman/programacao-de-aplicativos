import sqlite3

def cadastrar_turma(nome,id_serie,id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_keys = ON;")
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)"), (nome , id_serie , id_prof)
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor ou série não existe.")
    finally:
        conexao.close()

# pode ocorrer um erro por conta que não o id prof não está existente  entao colocamos os try, except junto com o erro que em seguida ele vai aparecer
# se tiver um eero o commit e o close não são executado
