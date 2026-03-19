vagas = ["livre" , "ocupado" , "livre" , "ocupado"]
vaga = int(input("digite o numero da vaga de 0 a 3: ")) 

if 0 <= vaga < 3:
    if vaga %  2 == 0 and vagas[vaga] == "livre": 
        print(f"vaga {vaga} autorizada para estacionar")
    
    else:
        print(f"vagas {vaga} indisponivel ou fora das regras") 
else:
    print("vagas invalidas") 