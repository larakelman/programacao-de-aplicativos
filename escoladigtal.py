




    
     import json  # ele importa o módulo json
import os # ele importa os módulos os 

BANCO_DADOS = 'alunos.json' # para criar a váriavel com o nome de arquivo onde vão ser salvos 

def cadastrar(): # cria a função pedida 
    print("\n--- Novo Cadastro ---") # mostra o titulo e \n pula as linhas 
    
    if os.path.exists(BANCO_DADOS): # ele pergunta se o arquivo existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # passa o arquivo para o modo de leitura 
            alunos = json.load(f) # le o arquivo json e transforma em lista 
    else: # mantem a primeira condição 
        alunos = [] # quando o arquivo não existe ele cria um lista vazia 

    novo_aluno = { # cria um dicionario com os dados do aluno 
        "nome": input("Nome: "), # pede o nome do aluno 
        "telefone": input("Telefone: "), # pede o telefone do aluno 
        "idade": int(input("Idade: ")), # pede a idade do aluno 
        "cpf": input("CPF: ") # pede o cpf do aluno 
    }
    
    alunos.append(novo_aluno)  # adiciona um novo aluno na sua lista 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # deixe o arquivo em modo escrita 
        json.dump(alunos, f, indent=4, ensure_ascii=False) # salva os dados no arquivo json 
        
    print("Aluno cadastrado com sucesso!") # mostre a mensagem que o aluno foi cadastrado com sucesso 

def listar(): # função que vai listar os alunos 
    print("\n--- Lista de Alunos ---") # ele é o titulo
    
    if os.path.exists(BANCO_DADOS): # verifica se á existenssia no arquivo 
         with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # ele abrirá o seu arquivo 
            alunos = json.load(f) # le os dados do arquivo json 
    else:
        alunos = [] # quando o arquivo não existe ele cria uma lista vazia 

    if not alunos: # verifica se a lista está vazia ou não 
        print("Nenhum aluno cadastrado.") # mensagem que ele não encontrou nennhum aluno encontrado 
        return # vai encerrar a sua função 

    for aluno in alunos: # ve todos os alunos da sua lista 
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # mostra cada dado de cada aluno 

def atualizar(): # ele irá atualizar a sua função 
    print("\n--- Atualizar Aluno ---") # mostra seu titulo 
    if not os.path.exists(BANCO_DADOS): # verifica se o arquivo existe ou não 
        print("Nenhum aluno cadastrado no sistema.") # mensagem que mostra quando não acha nenhum aluno cadastrado
        return # encerra sua função 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre seu arquivo 
        alunos = json.load(f) # carrega os alunos do arquivo 
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") # pede o cpf do aluno 
    
    for aluno in alunos: # ve todos seus alunos 
        if aluno['cpf'] == cpf_busca: # verifica se o cpf é o mesmo 
            print(f"Editando dados de: {aluno['nome']}") # mostra o nome do aluno que foi encontrado 
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # atualiza o nome do aluno 
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] # atualiza o seu telefone 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # atualiza a turma do aluno 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # atualiza a idade do aluno 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # atualiza o cpf do aluno 
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo e como ele para o modo escrita 
                json.dump(alunos, f, indent=4, ensure_ascii=False) # salva suas interações 
            print("Dados atualizados com sucesso!") # mensagem que diz que os dados foram atualizados com sucesso 
            return # encerra sua função 
            
    print("Aluno não encontrado.") # caso ele não acha o cpf do aluno 

def excluir(): # função que vai excluir 
    print("\n--- Excluir Aluno ---") # mostra o titulo do arquivo 
    if not os.path.exists(BANCO_DADOS): # verifica se o arquivo existe mesmo 
        print("Nenhum aluno cadastrado no sistema.") # mensagem que não tem nenhum aluno cadastrado no sistema 
        return # encerra sua função 

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre seu arquivo 
        alunos = json.load(f) # carrega todos os alunos do arquivo 
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ") # pergunta qual cpf o aluno deseja remover 
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca] # cria nova lista sem ter aluno resolvido, percorre os alunos e tem cpfs apenas que são diferentes 
     
    if len(nova_lista) < len(alunos): # ve se algum aluno foi removido da lista 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre um arquivo e coloca ele em modo escrita 
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # salva a sua nova lista 
        print("Aluno removido com sucesso!") # mnsagem que o aluno foi removido de sua lista com sucesso 
    else:
        print("Aluno não encontrado.") # mensagem que o aluno não foi encontrado 

def menu(): # seu menu principal 
    if not os.path.exists(BANCO_DADOS): # verifique se o arquivo existe mesmo 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # cria arquivo json quando ele está vazio 
            json.dump([], f) # salva lista quando está vazia 

    while True: # esse é o loop infinito 
        print("\n=== SISTEMA ESCOLAR ===") # mostra a mensagem sistema escolar 
        print("1. Cadastrar Aluno") # mostra a mensagem para cadastrar aluno 
        print("2. Listar Alunos") # mostra a mensagem listar alunos 
        print("3. Atualizar Aluno") # mostra a mensagem atualizar aluno 
        print("4. Excluir Aluno") # mostra mensagem excluir aluno 
        print("5. Sair") # mostra mensagems air 
        
        opcao = input("Escolha uma opção: ") # recebe as opções do usuario 
        
        if opcao == '1': cadastrar() # se escolher 1
        elif opcao == '2': listar() # se escolher 2
        elif opcao == '3': atualizar() # se escolher 3
        elif opcao == '4': excluir() # se escolher 4 
        elif opcao == '5': break # se escolher 5 
        else: print("Opção inválida!") # mostra a mensagem de "opção invalida"

menu() # inicia o seu sistema 