idade = float(input("digite sua idade: "))
saldo = float(input("digite seu saldo: "))

if idade >= 18  and saldo >= 50.00:
    print("acesso autorizado! bem vindo ao evento: ")

elif idade < 18 and saldo < 50.00:
    print("infelizmente voce nao cumpre os requisitos de entrada: ")
