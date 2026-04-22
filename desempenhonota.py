def avaliar_desempenho(nota):
    if nota >= 9:
        return "execelente"
    elif nota >= 7:
        return "bom"
    elif nota > 5:
        return "regular"
    else:
        return "insufuciente" 

nota = int(input("digite sua nota: "))
msg = avaliar_desempenho(nota)
print(msg) 
