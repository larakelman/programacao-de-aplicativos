def sofrer_dano(vida, dano):
    return vida - dano


# Programa principal
vida = 100

while vida > 0:
    dano = int(input("Digite o dano recebido: "))
    
    vida = sofrer_dano(vida, dano)
    print(f"Vida restante: {vida}")
    
    if vida <= 0:
        print("Game Over") 