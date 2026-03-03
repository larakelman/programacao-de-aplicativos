nome = input("digite seu nome: ")
usuario = input("qual seu usuario: ")
senha = int(input("digite sua senha: "))

if (usuario == "admins" or usuario == "root") and senha == 12345:
    print("acesso liberado")

else:
    print("acesso negado!") 
 