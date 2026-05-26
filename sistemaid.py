import json 

dados_alunos = "alunos.json" 

def cadastrar_aluno():
    print("\n ---cadastro do aluno---")

    if os.path.exists(dados_alunos):
        with open(dados_alunos, 'r', encoding='utf-8') as f:
            alunos = json.load(f) 
        
    else:
        alunos = [] 

    novo_aluno = { 
        "id": int(input("digite o id do seu aluno: "))
        "nome completo": int(input("digit o nome completo do aluno: "))
        "telefone": int(input("digite o telefone do aluno: "))
        "turma": int(input("digite a turma turma do aluno: "))
        "idade": int(input("digite a idade do aluno: "))
        "cpf": int(input("digite o cpf do aluno: ")) 
    } 

    if len(alunos) != 0:
        for aluno in alunos:
            if aluno["id"] == novo_aluno["id"]:
                print("id ja cadastrado!!")
                return

    alunos.append(novo_aluno)

    with open(dados_alunos, 'w', encoding= "utf-8") as f: 
        jsom.dump(alunos, f, indent = 4)

    print("aluno cadastrado com sucesso!") 

def listar_alunos(): 
    print("\n ---listar de alunos---")

    if os.path.exists(dados_alunos): 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos.json(load)

    else:
        lista[] 

    if not alunos:
        print("lista está vazia")
        return 

    for alunos in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") 

def atualizar_alunos(): 
    print("\n --- atualizar alunos ---")

    if os.path.exists(dados_alunos) 
