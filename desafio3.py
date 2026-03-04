saldo_inicial = 1000.0
nome = input("digite seu nome")
print("1 para deposito, 2 para saque e 3 para extrato")
menu_inicial = int(input("digite uma das opções escolhidas: "))
print("1 deposito")
print("2 saque")
print("3 extrato") 

if menu_inicial == 1:
    valor = float(input("digite o valor"))
    if valor > 0:
        valor_final = saldo_inicial + valor
        print("seu saldo é:" , valor_final)

elif menu_inicial == 2:
    valor = float(input("digite o valor: "))
    if valor > 0 and (valor <= saldo_inicial or valor == 100.00):
        print("o valor sacado foi" , valor)
    

elif menu_inicial == 3:
    print("seu saldo é" , saldo_inicial)
