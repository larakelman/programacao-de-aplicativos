lista_secreta = [123]
tentativas = 0 
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("tente adivinhar uma cor: ")

    if palpite in lista_secreta: 
        print("parabens, voce acertou! ")
        acertou = True 
    
    else:
        print("errou!") 

    tentativas += 1 
if not acertou:
    print("suas tentativas acabaram. ")
    print("as cores eram:" , lista_secreta) 