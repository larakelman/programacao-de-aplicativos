def calcular_area(largura, comprimento):
    return largura * comprimento


# Programa principal
contador = 0

while contador < 3:
    print(f"\nTerreno {contador + 1}")
    
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    
    area = calcular_area(largura, comprimento)
    
    print(f"Área do terreno: {area:.2f} m²")
    
    contador += 1 