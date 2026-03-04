cargo = input("Digite seu cargo: ")
codigo_de_acesso = int(input("Digite seu codigo de acesso: "))
botao_de_emergencia = input("botao de emergencia pressionado?: ")
epi = input("EPI completo?: ") 

if cargo == "engenheiro" or "tecnico" and (codigo_de_acesso == 1234 or botao_de_emergencia == "sim"): 
    print("acesso liberado") 
else:
    print("acesso negado: risco de segurança: ") 

