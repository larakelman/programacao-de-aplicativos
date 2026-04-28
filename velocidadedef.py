velocidade_km = float(input("digite a velocidade: "))
velocidade_ms = velocidade_km / 3.6

def converter_km_para_ms(velocidade_km, velocidade_ms):
    velocidade_ms = velocidade_km / 3.6
    if velocidade_km > 80:
        print("reduza a velocidade!") 
        return f"sua velocidade em ms é {velocidade_ms}"
    return f"sua velocidade em ms é {velocidade_ms}"

mensagem = converter_km_para_ms(velocidade_km, velocidade_ms)
print(mensagem) 