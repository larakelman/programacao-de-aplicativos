poder_de_ataque = float(input("digite seu poder de ataque:"))
ponto_de_defesa = float(input("digite seu ponto de desefa:"))

subtracao = poder_de_ataque - ponto_de_defesa

if subtracao <= 0:
    print("O vilao bloqueou o ataque! Dano 0")
elif subtracao > 0:
    print("ataque critico! voce causou dano ao vilao de" , subtracao)   

