usuario = input("digite o seu nome de usuario: ")
codigo = int(input("digite o codigo secreto: "))

if usuario == "admin" and codigo == 999: 
    print("acesso ao servidor liberado. Sistema online. ")
else: 
    print("falha na autenticacao. Alerta de segurnca ligado. ")